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
    price = models.IntegerField('Цена',null=True,blank=True)
    discount = models.IntegerField('Скидка',null=True,blank=True)
    # Добавил самостоятельно
    link_ps = models.OneToOneField(product_stock, on_delete=models.SET_NULL,null=True,blank=True)









