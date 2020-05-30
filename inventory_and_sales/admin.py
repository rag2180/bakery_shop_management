# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Customer, Order, Product, ProductOrder, Category

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(Category)
