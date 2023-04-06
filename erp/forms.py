from django import forms
from .models import Product, Inbound, Outbound


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'description', 'price', 'size']
        labels = {
            'name': '제품명',
            'code': '제품코드',
            'description': '설명',
            'price': '가격',
            'size': '사이즈'
        }


class InboundForm(forms.ModelForm):
    class Meta:
        model = Inbound
        fields = ['quantity']
        labels = {
            'quantity': '수량'
        }


class OutboundForm(forms.ModelForm):
    class Meta:
        model = Outbound
        fields = ['quantity']
        labels = {
            'quantity': '수량'
        }