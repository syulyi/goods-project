from django import forms
from .models import Product

class CompareProductForm(forms.Form):
    product1 = forms.ModelChoiceField(queryset=Product.objects.all(), label='Product 1')
    product2 = forms.ModelChoiceField(queryset=Product.objects.all(), label='Product 2')
    # products = forms.ModelMultipleChoiceField(
    #     queryset=Product.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    # )
