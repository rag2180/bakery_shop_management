# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Customer, Order, Product, Category, OrderItem, Ingredient, ProductIngredient, OverheadItem, ProductOverhead

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(ProductIngredient)
admin.site.register(OverheadItem)
admin.site.register(ProductOverhead)
