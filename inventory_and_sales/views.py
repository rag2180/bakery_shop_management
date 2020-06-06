# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import Product, ProductIngredient, ProductOverhead
from .forms import ProductForm, OrderItemForm, ProductIngredientForm, \
    ProductOverheadForm, OverheadItemForm, IngredientForm, CategoryForm


def home(request):
    products = Product.objects.all()
    print("ALLLL PRODUCTS.....")
    print(products)
    context = {'products': products}
    return render(request, 'inventory_and_sales/home.html', context)


def index(request):
    products = Product.objects.all()
    print("ALLLL PRODUCTS.....")
    print(products)
    context = {'products': products}
    return render(request, 'inventory_and_sales/base.html', context)


def products(request):
    products = Product.objects.all()
    print("ALLLL PRODUCTS.....")
    print(products)
    context = {'products': products}
    return render(request, 'inventory_and_sales/products.html', context)
    # return render(request, 'inventory_and_sales/list.html', context)


def order(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        print(dir(form))
        if form.is_valid():
            form.save()
            return redirect('order')
    else:
        form = OrderItemForm()
    return render(request, 'inventory_and_sales/add_product.html', {'form': form})


def detail(request, pk):
    print("Inside Detail...")
    product = get_object_or_404(Product, pk=pk)
    all_product_ingredients = ProductIngredient.objects.filter(product=product)
    all_product_overheads = ProductOverhead.objects.filter(product=product)
    print(product)
    print(all_product_ingredients)
    print(all_product_overheads)
    return render(request, 'inventory_and_sales/detail.html', {'product': product,
                                                               'ingredients': all_product_ingredients,
                                                               'overheads': all_product_overheads})


def add_product(request):
    return HttpResponseRedirect("Test Add Product")

# def add_product(request):
#     if request.method == 'POST':
#         product_form = ProductForm(request.POST)
#         product_ingredient_form = ProductIngredientForm()
#         product_ingredient_formset = ProductIngredientFormset()
#         print(dir(product_form))
#         if product_form.is_valid():
#             # product = form.save(commit=True)
#             product_form.save()
#
#             # product = Product()
#             # product.name = form.cleaned_data['name']
#             # product.cetagory = form.cleaned_data['cetagory']
#             # product.supplier = form.cleaned_data['supplier']
#             # product.unit_price = form.cleaned_data['unit_price']
#             # product.description = form.cleaned_data['description']
#             # product.save()
#             # return redirect('detail', pk=product.pk)
#             return redirect('index')
#     else:
#         product_form = ProductForm()
#         product_ingredient_form = ProductIngredientForm()
#         product_ingredient_formset = ProductIngredientFormset(queryset=ProductIngredient.objects.none())
#
#     return render(request, 'inventory_and_sales/add_product.html', {'product_form': product_form,
#                                                             'product_ingredient_form': product_ingredient_form,
#                                                         'product_ingredient_formset': product_ingredient_formset})
