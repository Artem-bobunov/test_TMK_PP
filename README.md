# ТЕСТОВОЕ ЗАДАНИЕ №1 

### Средства реализации приложения
- Djnago 3.2.11
- PostgreSQL
- Библиотека для работы с постгри psycopg2
- IDE: PyCharm

Для запуска проекта можно его склонировать и установить следующие зависимости
```
pip install -r requirements.txt
```
Затем зайти в первую папку test_set и выполнить следующую команду, которая сохрнаит все изменнения в отдельной папке migrations
```
python manage.py makemigrations
```
Далее необходимо выполнить миграции в базу данных. Эта команда применит все изменения которые были сохранены в миграциях
```
python manage.py migrate
```

Чтобы можно было использовать стандартную админку Django нужно в файле admin.py зарегистрировать модели как показано ниже:
```python
from django.contrib import admin
from .models import *

class DirectoryProduct(admin.ModelAdmin):
    list_display = ['name_product','price']

class DirectoryCounterparties(admin.ModelAdmin):
    list_display = ['contract']

class DocumentHeader(admin.ModelAdmin):
    list_display = ['number_document','date','summ_document','state_document','type_document']

class DocumentSpecification(admin.ModelAdmin):
    list_display = ['counts','counts_reserv','prices','discount']

class ProductStock(admin.ModelAdmin):
    list_display = ['count_fact','count_reserv']

# Register your models here.
admin.site.register(directory_product,DirectoryProduct)
admin.site.register(directory_counterparties,DirectoryCounterparties)
admin.site.register(document_header,DocumentHeader)
admin.site.register(document_specification,DocumentSpecification)
admin.site.register(product_stock,ProductStock)
```
Выполнить команду создания пользователя
```
python manage.py createsuperuser
```

Если все прошло успешно для запуска проекта необходимо выполнить следующую команду:
```
python manage.py runserver
```

Если зайти по адресу localhost:8000/admin/ ввести логин и пароль то перенаправит на страницу админки

![image](https://github.com/Artem-bobunov/test_TMK_PP/assets/38436717/e442358d-6039-401a-a16b-422d8abcb128)


## Создание базы данных и приложения

### Создание базы данных
В данном проекте я использовал Django ORM для создания базы данных. Структуру базы описана в моделях. Для связей между моделями я использовал OneToOneField.
Обратите внимание на поля которые добавил самотсоятельно, они имеют комментарий Добави.л самостоятельно

  ```python
  from django.db import models

class directory_product(models.Model):
    """Справочник товаров"""
    name_product = models.CharField('Наименование товара', max_length=255,null=True,blank=True)
    price = models.IntegerField('Цена',null=True,blank=True,default=0)

class directory_counterparties(models.Model):
    """Справочник контрагентов"""
    # Добавил самостоятельно
    contract = models.CharField('Наименование контракта', max_length=255, null=True, blank=True)

class document_header(models.Model):
    """Шапка документа"""

    number_document = models.IntegerField('Номер документа',null=True,blank=True)
    # ссылка на справочник контрагентов
    link_dc = models.OneToOneField(directory_counterparties, on_delete=models.SET_NULL,null=True,blank=True)
    date = models.DateField('Дата',auto_now = True)
    summ_document = models.IntegerField('Сумма документа',null=True)

class product_stock(models.Model):
    """Остатки товаров на складе"""

    # ссылка на справочник товаров
    link_dp = models.OneToOneField(directory_product, on_delete=models.SET_NULL,null=True,blank=True)
    count_fact = models.IntegerField('Количество фактическое',null=True,blank=True)
    count_reserv = models.IntegerField('Количество в резерве',null=True,blank=True)

class document_specification(models.Model):
    """Спецификация документов"""

    # ссылка на шапку документов
    link_dh = models.OneToOneField(document_header, on_delete=models.CASCADE,null=True,blank=True)
    # ссылка на справочник товаров
    link_dp = models.OneToOneField(directory_product, on_delete=models.SET_NULL,null=True,blank=True)
    counts = models.IntegerField('Количество',null=True,blank=True)
    counts_reserv = models.IntegerField('Количество в резерве',null=True,blank=True)
    prices = models.IntegerField('Цена',null=True,blank=True)
    discount = models.IntegerField('Скидка',null=True,blank=True)
    # Добавил самостоятельно
    link_ps = models.OneToOneField(product_stock, on_delete=models.SET_NULL,null=True,blank=True)
```

### Создание бекенд части
- На данном этапе реализовал две функции просмотра и редактирования инфорамции. Внесение записей осущевслялось как с помощью SQL так и с использованием Django Admin Panel
Функция просмотра всей инфорации принимает обязательный аргумент request:
```python
def list(request):
    obj = document_specification.objects.order_by('id')
    return render(request,'list.html',{'obj':obj})
```
- Функция обноления записи. В функцию я передаю аргумент id, который дальше исполуя чтобы найти в базе запись из таблицы document_specification, а далее по ключам прыгаю по другим таблицам чтобы найти данные и передать их в форму. Если request.method содержит POST, создаю объекты форм и в instance передаю значения которые ддолжна содержать эта форма. Проверяю не содержит ли формы ошибок при сохраненнии. Если формы валидны, сохраняю связынне формы, затем айдишникам для связки с другими таблицами присваиваю объект форм, это делается для того чтобы все связи между таблицами остались при изменении. далее сохраняю объекты форм и если все успешно сохранилось, то перехожу на главную страницу , иначе отработает блок Except и выведет ошибку.
```python
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
```

- Html код лежит в папке templates,
- Формы для заполнения полей представлены в файле forms.py,
- Маршрутизация представлена в файле urls.py,
- Все настройки проекта лежат в файле settings.py: подключение к БД, подключение проекта test_dev, настройка templates,

- Главная страница приложения
На этой странице пользователь может просматриват всю информацию связанных между собой таблиц.

Снимок экрана 2023-08-29 084508.png

![image](https://github.com/Artem-bobunov/test_TMK_PP/assets/38436717/dd09541b-6249-447c-9bca-3d104385c318)



- На главной странице выбираем интересующую запись и нажимаем на нее , затем попадем на страницу редактирования
Снимок экрана 2023-08-29 084421.png


![image](https://github.com/Artem-bobunov/test_TMK_PP/assets/38436717/233e76d8-c9f7-40c7-9160-11d9d9b1bf93)


# ТЕСТОВОЕ ЗАДАНИЕ №2
## Приход, резервирование и списание товара

- Обновленный код с реализацией алгоритмов:
```python

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
```

- Измененная модель, доавблены поля : состояние документа, тип документа.
```python

class document_header(models.Model):
    """Шапка документа"""

    choices_type = (
        ('Приход','Приход'),
        ('Резерв','Резерв'),
        ('Расход','Расход'),
    )

    number_document = models.IntegerField('Номер документа',null=True,blank=True)
    # ссылка на справочник контрагентов
    link_dc = models.OneToOneField(directory_counterparties, on_delete=models.SET_NULL,null=True,blank=True)
    date = models.DateField('Дата',auto_now = True)
    summ_document = models.IntegerField('Сумма документа',null=True)
    #Второе задание
    state_document = models.CharField('Состояние документа',max_length=255,null=True,blank=True)
    type_document = models.CharField('Тип документа', choices=choices_type,max_length=255,null=True,blank=True)
```
- Главная страница после обновления
  ![image](https://github.com/Artem-bobunov/test_TMK_PP/assets/38436717/c5928074-6575-4922-9795-68ed251a9674)



- Страница обновления данных



  ![image](https://github.com/Artem-bobunov/test_TMK_PP/assets/38436717/ee0ab30d-556a-4040-a4f8-95d1c342eca6)

  
    



