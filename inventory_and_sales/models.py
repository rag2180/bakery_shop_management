# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime


class Customer(models.Model):
    name = models.CharField(verbose_name="Name", help_text="Name of the customer", max_length=255, unique=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    address = models.CharField(verbose_name="Address", help_text="Address of Customer", default=None, null=True, max_length=255, blank=True)
    city = models.CharField(help_text="Name of City to which customer belongs", max_length=255, blank=True)
    email_id = models.EmailField(null=True, blank=True)
    date = models.DateField(help_text="Date when customer was acquired", null=True, auto_now_add=True)

    def __str__(self):
        return "{} | {}".format(self.name, self.phone_number)


class Category(models.Model):
    name = models.CharField(max_length=255, help_text="Category of a product. Eg: Cake, Biscuits etc.", unique=True)
    unit = models.CharField(max_length=255, help_text='Unit of measurement', choices=[('lb', 'pound'), ('gm', 'grams'),
                                        ('kg', 'kilogram'), ('pcs', 'piece')], default='kg')
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(help_text='Thing you use to create your product', max_length=255, unique=True)
    unit = models.CharField(choices=[("g", "gram"), ("ltr", "liter"), ("kg", "kilogram"), ("pc", "pieces"),
                                     ("tbsp", "table spoon"), ("tsp", "tea spoon")],
                            help_text="unit of measurement of this quantity", max_length=255, default="g")
    unit_cost = models.FloatField(verbose_name="Cost Price per unit")

    def __str__(self):
        return self.name+" | Rs."+str(self.unit_cost)+"/"+str(self.unit)


class OverheadItem(models.Model):
    name = models.CharField(help_text='Eg: Electricity, Labour, Packaging etc.', max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(help_text="Name of Item", max_length=255, unique=True)
    category = models.ForeignKey(Category, help_text="Category of this product item", on_delete=models.CASCADE)
    profit_percent = models.IntegerField(help_text='profit in % that you want from this product', default=0)
    cost_price = models.FloatField(help_text="This is calculated using ingredients and overheads of your product. "
                                             "This is cost price per unit.",
                                   null=True, blank=True)
    selling_price = models.FloatField(help_text="Calculated as per profit", null=False, blank=False, default=0.0)
    note = models.CharField(max_length=1000, help_text='Note for self about product', null=True, blank=True)

    def __str__(self):
        return self.name+" | Rs."+str(self.cost_price)+"/"+str(self.category.unit)

    def save(self, *args, **kwargs):
        self.cost_price = 0
        all_product_ingredients = ProductIngredient.objects.filter(product=self)
        all_product_overheads = ProductOverhead.objects.filter(product=self)

        for i in all_product_ingredients:
            ingredient_unit_cost = i.ingredient.unit_cost
            ingredient_quantity = i.quantity
            ingredient_total_cost = ingredient_unit_cost*ingredient_quantity
            self.cost_price += ingredient_total_cost

        for i in all_product_overheads:
            self.cost_price += i.cost

        self.selling_price = self.cost_price + (self.cost_price*(self.profit_percent/100.0))
        self.cost_price = round(self.cost_price)
        self.selling_price = round(self.selling_price)
        super(Product, self).save(*args, **kwargs)


class ProductIngredient(models.Model):
    """
    Stores quantity of every ingredient in every product
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(help_text="quantity of unit of this ingredient in a product")

    def __str__(self):
        return self.product.name+" | "+self.ingredient.name


class ProductOverhead(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    overheaditem = models.ForeignKey(OverheadItem, on_delete=models.CASCADE)
    cost = models.FloatField(help_text='Total Cost of overhead item')

    def __str__(self):
        return self.product.name+" | "+self.overheaditem.name+" | "+str(self.cost)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivery_status = models.BooleanField(help_text="Is the order delivered?")
    payment_status = models.BooleanField(help_text="Is the payment received from customer?")
    order_datetime = models.DateTimeField(name="Datetime", help_text="Date and time when order was placed", null=True, default=datetime.now())
    total_price = models.FloatField(verbose_name="Total Amount", default=0.0, null=True)
    timestamp = models.DateTimeField(auto_now=True)
    note_from_customer = models.CharField(max_length=255, help_text='Note from customers', null=True, blank=True)

    def __str__(self):
        return "{} | {} | {}".format(self.id, self.customer.name, self.total_price)


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(help_text="units of product sold to customer", null=False, default=1)

    def __str__(self):
        return "{} | {}".format(self.order_id, self.product_id)

    def save(self, *args, **kwargs):
        self.order_id.total_price += (self.product_id.selling_price * self.quantity)
        self.order_id.save(*args, **kwargs)
        super(OrderItem, self).save(*args, **kwargs)
