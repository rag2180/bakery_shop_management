# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from  django.forms import modelformset_factory, inlineformset_factory

from .models import Product, ProductIngredient, ProductOverhead
from .forms import ProductForm, OrderItemForm, ProductIngredientForm, \
    ProductFormset


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


def edit_product(request, product_id):
    print("Inside edit product with id - {}".format(product_id))
    product = get_object_or_404(Product, id=product_id)
    print(product)
    if request.method == "POST":
        product_form = ProductForm(request.POST, instance=product)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.save()
            redirect_path = '/add_ingredient_of_product/{}'.format(product.id)
            return redirect(redirect_path, product_id=product.id)
    else:
        product_form = ProductForm(instance=product)
    # return HttpResponse("Inside edit product with id - {}".format(product_id))
    return render(request, 'inventory_and_sales/add_product.html', {'product_form': product_form})


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
    if request.method == 'POST':
        print("Post Request")
        product_form = ProductForm(request.POST)
        # print(product_form)
        print(product_form.is_valid())
        if product_form.is_valid():
            print("Form is Valid")
            print(product_form.cleaned_data)
            product_name = product_form.cleaned_data['name']
            product_category = product_form.cleaned_data['category']
            profit_percent = product_form.cleaned_data['profit_percent']
            note = product_form.cleaned_data['note']
            product = Product.objects.create(name=product_name, category=product_category, profit_percent=profit_percent,
                                          note=note)
            print(product)
            redirect_path = 'add_ingredient_of_product/{}'.format(product.id)
            return redirect(redirect_path, product_id=product.id)
        else:
            product_form = ProductForm()
            return render(request, 'inventory_and_sales/add_product.html', {'alert': True, 'product_form': product_form})

    else:
        product_form = ProductForm()

    return render(request, 'inventory_and_sales/add_product.html', {'product_form': product_form})


def add_ingredient_of_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    ProductIngredientFormset = inlineformset_factory(Product, ProductIngredient, fields=('ingredient', 'quantity',))

    if request.method == "POST":
        formset = ProductIngredientFormset(request.POST, instance=product)
        if formset.is_valid():
            formset.save()
            product.save()
            return redirect('inventory_and_sales/add_ingredient', product_id=product.id)

    formset = ProductIngredientFormset(instance=product)
    return render(request, 'inventory_and_sales/add_ingredient.html', {'formset': formset,
                                                                       'product': product,
                                                                       'type': 'Ingredients'})

def add_overhead_of_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    ProductOverheadFormset = inlineformset_factory(Product, ProductOverhead, fields=('overheaditem', 'cost',))

    if request.method == "POST":
        formset = ProductOverheadFormset(request.POST, instance=product)
        if formset.is_valid():
            formset.save()
            product.save()
            return redirect('inventory_and_sales/add_overhead', product_id=product.id)

    formset = ProductOverheadFormset(instance=product)
    return render(request, 'inventory_and_sales/add_overhead.html', {'formset': formset,
                                                                       'product': product,
                                                                       'type': 'Overheads'})
