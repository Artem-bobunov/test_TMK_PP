from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def list(request):
    obj = document_specification.objects.all()
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

                # Связывание связанных объектов с объектом document_specification
                obj.link_dh = link_dh_instance
                obj.link_dp = link_dp_instance
                obj.link_ps = link_ps_instance
                link_dh_instance.link_dc = link_dh_link_dc_instance
                link_dh_instance.save()

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
