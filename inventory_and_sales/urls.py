from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^products', products, name="products"),
    url(r'^orders', orders, name="orders"),
    url(r'^customers', customers, name="customers"),
    url(r'^customer/(?P<customer_id>\d+)/', customer_detail, name="customer_detail"),
    url(r'^edit_customer/(?P<customer_id>\d+)/edit/', edit_customer, name="edit_customer"),
    url(r'^edit_order/(?P<order_id>\d+)/edit/', edit_order, name="edit_order"),
    url(r'^order/(?P<order_id>\d+)/', order_detail, name="order_detail"),
    url(r'^add_customer', add_customer, name="add_customer"),
    url(r'^add_order', add_order, name="add_order"),
    url(r'^ingredients_and_overheads', ingredients_and_overheads, name="ingredients_and_overheads"),
    url(r'^create_ingredient', create_ingredient, name="create_ingredient"),
    url(r'^create_overheads', create_overheads, name="create_overheads"),
    url(r'^create_category', create_category, name="create_category"),
    url(r'^(?P<pk>\d+)$', detail, name="detail"),
    url(r'^add_product', add_product, name="add_product"),
    url(r'^add_ingredient_of_product/(?P<product_id>\d+)/', add_ingredient_of_product, name="add_ingredient_of_product"),
    url(r'^add_items_of_order/(?P<order_id>\d+)/', add_items_of_order, name="add_items_of_order"),
    url(r'^add_overhead_of_product/(?P<product_id>\d+)/', add_overhead_of_product, name="add_overhead_of_product"),
    url(r'^product/(?P<product_id>\d+)/edit/', edit_product, name="edit_product"),
    url(r'^ingredient/(?P<ingredient_id>\d+)/edit/', edit_ingredient, name="edit_ingredient"),
    url(r'^overhead/(?P<overhead_id>\d+)/edit/', edit_overhead, name="edit_overhead"),
    url(r'^category/(?P<category_id>\d+)/edit/', edit_category, name="edit_category")
]
