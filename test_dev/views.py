from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def list(request):
    obj = document_specification.objects.order_by('id')
    return render(request,'list.html',{'obj':obj})

def update(request,id):
    obj = document_specification.objects.get(id=id)
    link_dh_instance = obj.link_dh
    link_dp_instance = obj.link_dp
    link_ps_instance = obj.link_ps
    link_dh_link_dc_instance = obj.link_dh.link_dc

    if request.method == 'POST':
        form = FormDocumentSpecification(request.POST, instance=obj)
        form1 = FormDocumentHeader(request.POST, instance=link_dh_instance)
        form2 = FormDirectoryProduct(request.POST, instance=link_dp_instance)
        form3 = FormProductStock(request.POST, instance=link_ps_instance)
        form4 = FormDirectoryCounterparties(request.POST,instance=link_dh_link_dc_instance)
        if form.errors:
            print(f'Форма 0 {form.errors}')
        if form1.errors:
            print(f'Форма 1 {form1.errors}')
        if form2.errors:
            print(f'Форма 2 {form2.errors}')
        if form3.errors:
            print(f'Форма 3 {form3.errors}')
        if form4.errors:
            print(f'Форма 4 {form4.errors}')
        if form.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            print('ФОРМА ВАЛИДНА')
            try:
                # form.save()
                # Сохранение связанных форм
                link_dh_instance = form1.save()
                link_dp_instance = form2.save()
                link_ps_instance = form3.save()
                link_dh_link_dc_instance = form4.save()

                """Алгоритм приходования доступен для документа «приход» с «состоянием
                документа», отличном от «Оприходовано». При выполнении алгоритма
                приходования для каждой строчки в документе на величину поля «количество»
                увеличивается величина поля «количество» в таблице складских остатков.
                Полю «состояние документа» присваивается значение «Оприходовано»."""

                if form1.cleaned_data['type_document'] == 'Приход':
                    link_ps_instance.count_fact += form.cleaned_data['counts']
                    link_ps_instance.count_reserv += form.cleaned_data['counts']

                """Алгоритм отмены прихода доступен для документа «приход» с «состоянием
                документа» «Оприходовано». При выполнении алгоритма для каждой
                строчки в документе на величину поля «количество» уменьшается величина
                поля «количество» в таблице складских остатков. Полю «состояние
                документа» присваивается значение «Черновик»."""
                if form1.cleaned_data['type_document'] == 'Приход' and form1.cleaned_data['state_document'] == 'Оприходовано':
                    link_dh_instance.state_document = 'Черновик'
                    link_ps_instance.count_fact -= form.cleaned_data['counts']
                    link_ps_instance.count_reserv -= form.cleaned_data['counts']

                """Алгоритм резервирования доступен для документа «резерв» в любом
                состоянии. При выполнении алгоритма резервирования для каждой позиции в
                документе анализируется разница между значениями полей «количество» и
                «количество в резерве». На величину этой разницы для товара из строчки
                документа нужно увеличить значение поля «количество в резерве» в таблице
                складских остатков, но таким образом, чтобы не превысить значение поля
                «количество фактическое». На величину количества, которое удалось
                зарезервировать, нужно увеличить значение поля «количество в резерве» для
                строчки документа. Полю «состояние документа» присваивается значение
                «Зарезервировано»."""
                if form1.cleaned_data['type_document'] == 'Резерв':
                    # разницу между значениями полей "количество" и "количество в резерве"
                    difference = form.cleaned_data['counts'] - form3.cleaned_data['count_reserv']
                    # Увеличить значение поля количество в резерве на величину этой разницы
                    # но не превышая значение поля количестов фактическое из таблицы скласдких документов
                    sum_cr = form3.cleaned_data['count_reserv'] + difference
                    if sum_cr > form3.cleaned_data['count_reserv']:
                        link_ps_instance.count_reserv = sum_cr - form3.cleaned_data['count_reserv']
                    else:
                        link_ps_instance.count_reserv = sum_cr
                    link_dh_instance.state_document = 'Зарезервировано'
                """Алгоритм отмены резервирования доступен для документа «резерв» в
                состоянии «Зарезервивровано» и выполняет обратную операцию -
                уменьшает до нуля значение поля «количество в резерве для строчки
                документа» и на такую же величину уменьшает для соответствующего
                товара значение поля в таблице складских остатков. Полю «состояние
                документа» присваивается значение «Черновик»."""
                if form1.cleaned_data['type_document'] == 'Резерв' and form1.cleaned_data['state_document'] == 'Зарезервивровано':
                    obj.counts_reserv = 0
                    link_ps_instance.count_reserv = 0
                """Алгоритм списания доступен для документа «расход» с «состоянием
                документа», отличном от «Списано». При выполнении алгоритма для каждой
                строчки в документе на величину поля «количество» уменьшается величина
                полей «количество ФАКТИЧЕСКОЕ?» и «количество в резерве» в таблице складских остатков.
                Если при этом любая из величин в таблице складских остатков оказывается
                меньше нуля, то происходит полная отмена операции для всего документа.
                При успешной операции списания полю «состояние документа»
                присваивается значение «Списано»."""
                if form1.cleaned_data['type_document'] == 'Расход' and form1.cleaned_data['state_document'] == 'Списано':
                    obj1 = form3.cleaned_data['count_fact'] - obj.counts
                    obj2 = form3.cleaned_data['count_reserv'] - obj.counts
                    if obj1 or obj2 > 0:
                        link_ps_instance.count_fact = obj1
                        link_ps_instance.count_reserv = obj2
                        link_dh_instance.state_document = 'Списано'
                """Алгоритм отмены списания доступен для документа «списание» с
                «состоянием документа» «Списано». При выполнении алгоритма для
                каждой строчки в документе на величину поля «количество»
                увеличивается величина поля «количество» в таблице складских остатков.
                Полю «состояние документа» присваивается значение («Черновик»)."""
                if form1.cleaned_data['state_document'] == 'Списано':
                    link_ps_instance.count_fact += obj.counts
                    link_dh_instance.state_document = 'Черновик'

                # Связывание связанных объектов с объектом document_specification
                obj.link_dh = link_dh_instance
                obj.link_dp = link_dp_instance
                obj.link_ps = link_ps_instance
                link_dh_instance.link_dc = link_dh_link_dc_instance
                link_dh_instance.save()
                link_dp_instance.save()
                link_ps_instance.save()

                obj.save()

                return redirect('/')
            except Exception as e:
                print(f'ОШИБКА: {e}')
    else:
        form = FormDocumentSpecification(instance=obj)
        form1 = FormDocumentHeader(instance=link_dh_instance)
        form2 = FormDirectoryProduct(instance=link_dp_instance)
        form3 = FormProductStock(instance=link_ps_instance)
        form4 = FormDirectoryCounterparties(instance=link_dh_link_dc_instance)

    return render(request,'update.html',{'form':form,'form1':form1,'form2':form2,'form3':form3,'form4':form4})
