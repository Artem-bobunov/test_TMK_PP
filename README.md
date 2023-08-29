# ТЕСТОВОЕ ЗАДАНИЕ №1 
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
На данном этапе реализовал две функции просмотра и редактирования инфорамции. Внесение записей осущевслялось как с помощью SQL так и с использованием Django Admin Panel
- Функция просмотра всей инфорации принимает обязательный аргумент request:
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


- Главная страница приложения
На этой странице пользователь может просматриват всю информацию связанных между собой таблиц.


[![Главная страница](https://github.com/Artem-bobunov/test_TMK_PP/assets/38436717/d7d709d5-797e-4668-84e5-08c424cdde0c)]



- На главной странице выбираем интересующую запись и нажимаем на нее , затем попадем на страницу редактирования


[![Страница обновления](https://github.com/Artem-bobunov/test_TMK_PP/assets/38436717/418e09a4-ff46-427e-bd6d-7a9ba43bbe70)]






