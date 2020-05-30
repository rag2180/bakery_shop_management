# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models


class Customer(models.Model):
    name = models.CharField(verbose_name="Name", help_text="Name of the customer", max_length=255, unique=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    address = models.CharField(verbose_name="Address", help_text="Address of Customer", default=None, null=True, max_length=255)
    city = models.TextField(help_text="Name of City to which customer belongs", max_length=255)
    email_id = models.EmailField(null=True)
    date = models.DateField(help_text="Date when customer was acquired", null=True, auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=255, help_text="Category of a product. Eg: Raw/Final")
    description = models.CharField(max_length=255, null=True)


class Product(models.Model):
    name = models.CharField(help_text="Name of Item", max_length=255, unique=True)
    category = models.ForeignKey(Category, help_text="Category of this product item")
    quantity = models.IntegerField(help_text="Quantity of item stored")
    unit = models.CharField(help_text="units of quantity", max_length=255)
    cost_price = models.IntegerField(name="Cost Price", help_text="Cost of your own purchase or cost of production of this product", null=True)
    selling_price = models.IntegerField(name="Selling Price", help_text="Selling price of product", null=True)


class Order(models.Model):
    customer_id = models.ForeignKey(Customer)
    delivery_status = models.BooleanField(help_text="Is the order delivered?")
    payment_status = models.BooleanField(help_text="Is the payment received from customer?")
    total_amount = models.IntegerField(name="Order Value")


class ProductOrder(models.Model):
    order_id = models.ForeignKey(Order)
    product_id = models.ForeignKey(Product)
    quantity = models.IntegerField(name="Quantity", help_text="units of product sold to customer", null=True)
    price = models.IntegerField(name="Price", help_text="This is product of product price and quantity", null=True)


