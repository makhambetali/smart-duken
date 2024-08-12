from django import forms
from .models import *
from django.core.validators import MaxLengthValidator
from django.utils import timezone
from datetime import timedelta
from django.forms import ClearableFileInput


class ProductForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': timezone.now(
        ).date(), 'max': timezone.now().date()+timedelta(days=30)}),
        label='Дата прихода',
        error_messages={
            'min_value': 'Дата прихода не может быть раньше сегодняшней даты.',
            'max_value': 'Дата прихода не может быть более чем через 30 дней от сегодняшней даты.'
        }
    )

    class Meta:
        model = Product
        fields = ['cost', 'bonus', 'exchange', 'comment', 'date']
        # exclude = ['name','cost', 'confirmed', 'creator','payment']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'cost': forms.TextInput(attrs={'class': 'currency-mask', 'inputmode': 'numeric', 'minlength': 2, 'maxlength':9}),
            'bonus': forms.NumberInput(attrs={'max': '999', 'min': 0, 'oninput':'length_slice(this)'}),
            'exchange': forms.NumberInput(attrs={'max': '999', 'min': 0, 'oninput':'length_slice(this)'}),
            # 'comment':forms.Textarea(attrs={'maxlength': '200'})


        }


class SupplyEditForm(ProductForm):
    class Meta:
        model = Product
        fields = ['cost', 'bonus',
                  'exchange', 'comment', 'date', 'confirmed', 'payment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'cost': forms.TextInput(attrs={'class': 'currency-mask', 'inputmode': 'numeric', 'minlength': 2}),
            'bonus': forms.NumberInput(attrs={'max': '999', 'min': 0, 'oninput':'length_slice(this)'}),
            'exchange': forms.NumberInput(attrs={'max': '999', 'min': 0, 'oninput':'length_slice(this)'})

        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        exclude = ['creator']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'ex: Фудмастер','required':True}),
            'tel_number_supervisor': forms.TextInput(attrs={'class': 'tel-number-mask', 'inputmode': 'numeric', 'minlength': 2, 'placeholder': '+{7}(000)000-00-00'}),
            'tel_number_salesman': forms.TextInput(attrs={'class': 'tel-number-mask', 'inputmode': 'numeric', 'minlength': 2, 'placeholder': '+{7}(000)000-00-00'}),
            'tel_number_delivery': forms.TextInput(attrs={'class': 'tel-number-mask', 'inputmode': 'numeric', 'minlength': 2, 'placeholder': '+{7}(000)000-00-00'}),
            
            'extra_info':forms.Textarea(attrs={'maxlength': '200'})


        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        widgets = {
           'image':forms.FileInput(attrs={'onchange':'previewImage(this)',"accept":"image/png, image/jpeg"})


        }

class DebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        exclude = ['client','creator']
        widgets = {
            'content': forms.TextInput(attrs={'class': 'moneyInput', 'inputmode': 'numeric', 'minlength': 2,'oninput':"check_length('.updateData',this.value)"}),

            # 'comment':forms.Textarea(attrs={'maxlength': '200'})


        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone_number', 'about', 'is_chosen']
        widgets = {
            'name':forms.TextInput(attrs={'required':True})


        }


class MoneyForm(forms.ModelForm):
    class Meta:
        model = Money
        fields = ['content','text']
        widgets = {
            'content': forms.TextInput(attrs={'class': 'moneyInput', 'inputmode': 'numeric', 'minlength': 2,'oninput':"check_length('.updateData',this.value)"}),

            # 'comment':forms.Textarea(attrs={'maxlength': '200'})


        }