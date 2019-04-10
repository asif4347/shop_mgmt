from pprint import pprint
from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.forms import ModelForm, inlineformset_factory
# from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget


class AddSalesmanForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'write name'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':15,'class':'form-control'}))

    class Meta:
        model = Salesman

        exclude = ['shops']


class AddOrderForm(forms.ModelForm):
    salesman = forms.ModelChoiceField(queryset=Salesman.objects.all())
    # status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}))
    date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'datepicker col-xs-6','type':'date'}))

    class Meta:
        model = Orders
        fields = ('__all__')

    # def __init__(self, *args, **kwargs):
    #     super(AddOrderForm, self).__init__(*args, **kwargs)
    #     self.fields["products"].widget = forms.widgets.CheckboxSelectMultiple()
    #     self.fields["products"].queryset = Product.objects.all()


class AddShopForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'write name'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 15, 'class': 'form-control'}))

    class Meta:
        model = Shop
        fields = ('__all__')


class AddAmountForm(forms.ModelForm):
    # timestamp = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    timestamp = forms.DateField(widget=forms.SelectDateWidget(attrs = {'class': 'datepicker col-xs-6'}))
    # timestamp = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # timestamp = forms.DateField(widget=forms.TextInput(attrs=
    # {
    #     'class': 'datepicker'
    # }))
    class Meta:

        model = Amount
        exclude = ['delivery']

    def __init__(self, *args, **kwargs):
        self.order = kwargs.pop("order", '')
        super(AddAmountForm, self).__init__(*args, **kwargs)

    def clean_amount(self):
        total_amount = self.order.total_amount
        paid_amount = self.order.amount_paid
        amount = self.cleaned_data['amount']
        total = paid_amount + amount
        if total > total_amount:
            remaining = total_amount-paid_amount
            if remaining == 0:
                raise ValidationError("Order amount is completed.")
            else:
                raise ValidationError("Remaining amount: {0}".format(total_amount-paid_amount))
        else:
            self.order.amount_paid += amount
            self.order.save()
            if total_amount == paid_amount:
                self.order.status = Orders.com
                self.order.save()
        return amount


class OrderForm(ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'datepicker col-xs-6'}))

    class Meta:
        model = Orders
        exclude = ()


class FamilyMemberForm(ModelForm):

    class Meta:
        model = OrderProducts
        exclude = ()


# OrderProductFormSet = inlineformset_factory(Orders, OrderProducts,
#                                             form=OrderProductForm, extra=1)


from django.forms import BaseInlineFormSet

class CustomInlineFormSet(BaseInlineFormSet):
    def clean(self):
        error_list = []
        super(CustomInlineFormSet, self).clean()
        # example custom validation across forms in the formset
        for form in self.forms:
            # your custom formset validation

            item = form.cleaned_data.get('item', '')
            if item:
                quantity = form.cleaned_data['quantity']

                # quantity = form.cleaned_data.get('quantity', '')
                print(type(quantity))
                if quantity <= item.quantity_in_stock:
                    item.quantity_in_stock = item.quantity_in_stock-quantity
                    item.save()
                    pprint(item)
                else:
                    # raise ValidationError('only {0} items of {1} in stock'.format(item.quantity_in_stock, item.name))
                    error_list.append('only {0} items of {1} in stock'.format(item.quantity_in_stock, item.name))
                    # form.add_error("item", 'only {0} items of {1} in stock'.format(item.quantity_in_stock, item.name))
                    # form.add_error('', 'only {0} items of {1} in stock'.format(item.quantity_in_stock, item.name))
        if error_list:
            raise ValidationError(error_list)


FamilyMemberFormSet = inlineformset_factory(Orders, OrderProducts,
                                            form=FamilyMemberForm, formset=CustomInlineFormSet, extra=1)



#
# class CustomInlineFormSet(BaseInlineFormSet):
#     def clean(self):
#         error_list = []
#         super(CustomInlineFormSet, self).clean()
#         # example custom validation across forms in the formset
#         for form in self.forms:
#             # your custom formset validation
#
#             item = form.cleaned_data.get('item', '')
#             if item:
#                 quantity = form.cleaned_data['quantity']
#
#                 # quantity = form.cleaned_data.get('quantity', '')
#                 print(type(quantity))
#                 if quantity <= item.quantity_in_stock:
#                     item.quantity_in_stock = item.quantity_in_stock-quantity
#                     item.save()
#                     pprint(item)
#                 else:
#                     error_list.append('only {0} items of {1} in stock'.format(item.quantity_in_stock, item.name))
#                     # form.add_error("item", 'only {0} items of {1} in stock'.format(item.quantity_in_stock, item.name))
#                     # form.add_error('', 'only {0} items of {1} in stock'.format(item.quantity_in_stock, item.name))
#         if error_list:
#             raise ValidationError(error_list)
#
