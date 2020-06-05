from django.forms import ModelForm
from .models import Product, OrderItem


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category']


class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'
