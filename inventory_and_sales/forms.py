from django.forms import ModelForm
from .models import Product, OrderItem, Category, Ingredient, OverheadItem, ProductIngredient, ProductOverhead
from django.forms import modelformset_factory
from  django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'profit_percent', 'note']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'


class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OverheadItemForm(ModelForm):
    class Meta:
        model = OverheadItem
        fields = '__all__'


class ProductIngredientForm(ModelForm):
    class Meta:
        model = ProductIngredient
        fields = ['ingredient', 'quantity']


class ProductOverheadForm(ModelForm):
    class Meta:
        model = ProductOverhead
        fields = '__all__'


# ProductIngredientFormset = modelformset_factory(
#     ProductIngredientForm,
#     fields=('ingredient', 'quantity'),
#     extra=1,
#     widgets={'name': forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter Ingredient for this product'
#         })
#     }
# )