from django import forms
from .models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        # fields = ["first_name","last_name","phone_number","address","email","customer_image"]
        exclude = [""]


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        exclude = [""]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = [""]


class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        exclude = ["profit"]
