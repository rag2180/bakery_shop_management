# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from  django.forms import formset_factory, inlineformset_factory

from .models import Product, ProductIngredient, ProductOverhead, Ingredient, Customer
from .forms import ProductForm, OrderItemForm, ProductIngredientForm, \
    ProductFormset, IngredientForm, OverheadItem, OverheadItemForm, CustomerForm


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


def ingredients_and_overheads(request):
    print("inside ingredients_and_overheads")
    ingredients = Ingredient.objects.all()
    overheads = OverheadItem.objects.all()
    print("All INGREDIENTS and Overheads.....")
    print(ingredients)
    context = {'ingredients': ingredients,
               'overheads': overheads}
    return render(request, 'inventory_and_sales/ingredients.html', context)


def customers(request):
    print("inside customers")
    customers = Customer.objects.all()
    return render(request, 'inventory_and_sales/customers.html', {'customers': customers})


def add_customer(request):
    print("inside add_customer")
    if request.method == 'POST':
        print("Post Request")
        customer_form = CustomerForm(request.POST)
        # print(product_form)
        print(customer_form.is_valid())
        if customer_form.is_valid():
            print("Form is Valid")
            print(customer_form.cleaned_data)
            customer_name = customer_form.cleaned_data['name']
            phone_number = customer_form.cleaned_data['phone_number']
            address = customer_form.cleaned_data['address']
            city = customer_form.cleaned_data['city']
            email_id = customer_form.cleaned_data['email_id']
            date = datetime.now()
            customer = Customer.objects.create(name=customer_name, phone_number=phone_number,
                                             address=address, email_id=email_id,
                                             city=city, date=date)
            print(customer)
            return redirect("customers")
        else:
            customer_form = CustomerForm()
            return render(request, 'inventory_and_sales/add_customer.html',
                          {'alert': True, 'customer_form': customer_form})

    else:
        customer_form = CustomerForm()

    return render(request, 'inventory_and_sales/add_customer.html', {'customer_form': customer_form})


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


def edit_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    print(ingredient)
    if request.method == "POST":
        ingredient_form = IngredientForm(request.POST, instance=ingredient)
        if ingredient_form.is_valid():
            ingredient = ingredient_form.save(commit=False)
            ingredient.save()
            redirect_path = '/ingredients_and_overheads/'.format(ingredient.id)
            return redirect(redirect_path)
    else:
        ingredient_form = IngredientForm(instance=ingredient)

    return render(request, 'inventory_and_sales/create_ingredient.html', {'ingredient_form': ingredient_form})


def edit_overhead(request, overhead_id):
    overhead = get_object_or_404(OverheadItem, id=overhead_id)
    print(overhead)
    if request.method == "POST":
        overhead_item_form = OverheadItemForm(request.POST, instance=overhead)
        if overhead_item_form.is_valid():
            ingredient = overhead_item_form.save(commit=False)
            ingredient.save()
            redirect_path = '/ingredients_and_overheads/'.format(ingredient.id)
            return redirect(redirect_path)
    else:
        overhead_item_form = OverheadItemForm(instance=overhead)

    return render(request, 'inventory_and_sales/create_overhead.html', {'overhead_item_form': overhead_item_form})


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
    """
    Product Detail Page
    :param request:
    :param pk:
    :return:
    """
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

def customer_detail(request, customer_id):
    """
    Customer Detail Page
    :param request:
    :param customer_id:
    :return:
    """
    print("Inside customer detail")
    customer = get_object_or_404(Customer, id=customer_id)
    # TODO: Show all past orders by this customer
    return render(request, 'inventory_and_sales/customer_detail.html', {'customer': customer})


def edit_customer(request, customer_id):
    print("inside edit customer")
    customer = get_object_or_404(Customer, id=customer_id)
    print(customer)
    if request.method == "POST":
        customer_form = CustomerForm(request.POST, instance=customer)
        if customer_form.is_valid():
            ingredient = customer_form.save(commit=False)
            ingredient.save()
            redirect_path = '/customers/'
            return redirect(redirect_path)
    else:
        customer_form = CustomerForm(instance=customer)

    return render(request, 'inventory_and_sales/add_customer.html', {'customer_form': customer_form})


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


def create_ingredient(request):
    print("Creating Ingredient")

    if request.method == "POST":
        ingredient_form = IngredientForm(request.POST)
        if ingredient_form.is_valid():
                ingredient_form.save()
        else:
            print("INGREDIENT NOT VALID")
            return render(request, 'inventory_and_sales/create_ingredient.html', {'alert': True, 'ingredient_form': ingredient_form})

    ingredient_form = IngredientForm()
    return render(request, 'inventory_and_sales/create_ingredient.html', {'ingredient_form': ingredient_form})


def create_overheads(request):
    print("creating overheads")
    if request.method == "POST":
        overhead_item_form = OverheadItemForm(request.POST)
        if overhead_item_form.is_valid():
            overhead_item_form.save()
        else:
            print("form is not valid")
            return render(request, 'inventory_and_sales/create_overhead.html',
                          {'alert': True, 'overhead_item_form': overhead_item_form})
        return redirect('create_overheads')

    overhead_item_form = OverheadItemForm()
    return render(request, 'inventory_and_sales/create_overhead.html', {'overhead_item_form': overhead_item_form})


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
