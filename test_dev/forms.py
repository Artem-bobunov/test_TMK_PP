from django.forms import *
from .models import *
from django import forms


class FormDirectoryProduct(forms.ModelForm):
    """Справочник товаров"""
    class Meta:
        model = directory_product
        fields = "__all__"
        widgets = {
            'name_product': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class FormDirectoryCounterparties(forms.ModelForm):
    """Справочник контрагентов"""

    class Meta:
        model = directory_counterparties
        fields = "__all__"
        widgets = {
            'contract': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FormDocumentHeader(forms.ModelForm):
    """Шапка документа"""

    class Meta:
        model = document_header
        fields = "__all__"
        widgets = {
            'number_document': forms.NumberInput(attrs={'class': 'form-control'}),
            'summ_document': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control','type': 'date','format':'%d.%m.%Y'}),
            'state_document':TextInput(attrs={'class':'form-control'}),
            'type_document':Select(attrs={'class':'form-control'})
        }



class FormProductStock(forms.ModelForm):
    """Остатки товаров на складе"""

    class Meta:
        model = product_stock
        fields = "__all__"
        widgets = {
            'count_fact': forms.NumberInput(attrs={'class': 'form-control'}),
            'count_reserv': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class FormDocumentSpecification(forms.ModelForm):
    """ Форма отображения для моделей """

    class Meta:
        model = document_specification
        fields = "__all__"
        widgets = {
            'counts': forms.NumberInput(attrs={'class': 'form-control'}),
            'counts_reserv': forms.NumberInput(attrs={'class': 'form-control'}),
            'prices': forms.NumberInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    # def saves(self, commit=True):
    #     instance = super().save(commit=commit)
    #     print('+++++++++++++++++++++++++++++++++++++++++')
    #     print(instance.id)
    #     print(instance.link_ps.count_fact)
    #
    #     if instance.link_ps:
    #         print()
    #
    #         instance.link_ps = instance.id
    #         instance.link_ps.count_fact = self.cleaned_data.get('link_ps__count_fact', instance.link_ps.count_fact)
    #         instance.link_ps.count_reserv = self.cleaned_data.get('link_ps__count_reserv',
    #                                                               instance.link_ps.count_reserv)
    #         instance.link_ps.save()
    #
    #     if instance.link_dh:
    #         if instance.link_dh.link_dc:
    #             instance.link_dh.link_dc.contract = self.cleaned_data.get('link_dh__link_dc__contract',
    #                                                                       instance.link_dh.link_dc.contract)
    #             instance.link_dh.link_dc.save()
    #
    #         instance.link_dh.number_document = self.cleaned_data.get('link_dh__number_document',
    #                                                                  instance.link_dh.number_document)
    #         instance.link_dh.date = self.cleaned_data.get('link_dh__date', instance.link_dh.date)
    #         instance.link_dh.summ_document = self.cleaned_data.get('link_dh__summ_document',
    #                                                                instance.link_dh.summ_document)
    #         instance.link_dh.save()
    #
    #     if instance.link_dp:
    #         instance.link_dp.name_product = self.cleaned_data.get('link_dp_name_product', instance.link_dp.name_product)
    #         instance.link_dp.price = self.cleaned_data.get('link_dp_price', instance.link_dp.price)
    #         instance.link_dp.save()
    #     if commit:
    #         instance.save()
    #     return instance
    #
    #
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     instance = kwargs.get('instance')
    #
    #     # Форма для остатков товаров на складе
    #     if self.instance.link_ps:
    #         # self.fields['link_ps'].initial = instance.link_ps.id
    #
    #         self.fields['link_ps__count_fact'] = forms.IntegerField(
    #             label='Количество фактическое',
    #             initial=self.instance.link_ps.count_fact,
    #             widget=forms.NumberInput(attrs={'class': 'form-control'}),
    #             required=False
    #         )
    #         self.fields['link_ps__count_reserv'] = forms.IntegerField(
    #             label='Количество в резерве',
    #             initial=self.instance.link_ps.count_reserv,
    #             widget=forms.NumberInput(attrs={'class': 'form-control'}),
    #             required=False
    #         )
    #     # Форма для справочника контрагентов
    #     if self.instance.link_dh and self.instance.link_dh.link_dc:
    #         self.fields['link_dh__link_dc__contract'] = forms.CharField(
    #             label='Наименование контракта',
    #             initial=self.instance.link_dh.link_dc.contract,
    #             widget=forms.TextInput(attrs={'class': 'form-control'}),
    #             required=False
    #         )
    #     # форма для шапки документа
    #     if self.instance.link_dh:
    #         self.fields['link_dh__number_document'] = forms.IntegerField(
    #             label='Номер документа',
    #             initial=self.instance.link_dh.number_document,
    #             widget=forms.NumberInput(attrs={'class': 'form-control'}),
    #             required=False
    #         )
    #         self.fields['link_dh__date'] = forms.DateField(
    #             label='Дата',
    #             initial=self.instance.link_dh.date,
    #             widget=forms.TextInput(attrs={'class': 'form-control','type': 'date','format':'%d.%m.%Y'}),
    #             required=False
    #         )
    #         self.fields['link_dh__summ_document'] = forms.IntegerField(
    #             label='Сумма документа',
    #             initial=self.instance.link_dh.summ_document,
    #             widget=forms.NumberInput(attrs={'class': 'form-control'}),
    #             required=False
    #         )
    #     # Форма для справочника товаров
    #     if self.instance.link_dp:
    #         self.fields['link_dp_name_product'] = forms.CharField(
    #             label='Наименование товара',
    #             initial=self.instance.link_dp.name_product,
    #             widget=forms.TextInput(attrs={'class': 'form-control'}),
    #             required=False
    #         )
    #         self.fields['link_dp_price'] = forms.FloatField(
    #             label='Цена',
    #             initial=self.instance.link_dp.price,
    #             widget=forms.NumberInput(attrs={'class': 'form-control'}),
    #             required=False
    #         )
    #
    # link_ps = forms.ModelChoiceField(
    #     queryset=product_stock.objects.all(),
    #     widget=forms.Select(attrs={'class': 'form-control'}),
    #     label='Остатки товаров на складе',
    #     required=False
    # )
    # link_dp = forms.ModelChoiceField(
    #     queryset=directory_product.objects.all(),
    #     widget=forms.Select(attrs={'class': 'form-control'}),
    #     label='Справочник товаров',
    #     required=False
    # )
    # link_dh = forms.ModelChoiceField(
    #     queryset=document_header.objects.all(),
    #     widget=forms.Select(attrs={'class': 'form-control'}),
    #     label='Шапка документа',
    #     required=False
    # )



