from django.contrib import admin
from .models import *

class DirectoryProduct(admin.ModelAdmin):
    list_display = ['name_product','price']

class DirectoryCounterparties(admin.ModelAdmin):
    list_display = ['contract']

class DocumentHeader(admin.ModelAdmin):
    list_display = ['number_document','date','summ_document']

class DocumentSpecification(admin.ModelAdmin):
    list_display = ['counts','counts_reserv','price','discount']

class ProductStock(admin.ModelAdmin):
    list_display = ['count_fact','count_reserv']



# Register your models here.
admin.site.register(directory_product,DirectoryProduct)
admin.site.register(directory_counterparties,DirectoryCounterparties)
admin.site.register(document_header,DocumentHeader)
admin.site.register(document_specification,DocumentSpecification)
admin.site.register(product_stock,ProductStock)
