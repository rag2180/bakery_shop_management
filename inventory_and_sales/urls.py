from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^products', products, name="products"),
    url(r'^ingredients_and_overheads', ingredients_and_overheads, name="ingredients_and_overheads"),
    url(r'^create_ingredient', create_ingredient, name="create_ingredient"),
    url(r'^create_overheads', create_overheads, name="create_overheads"),
    url(r'^(?P<pk>\d+)$', detail, name="detail"),
    url(r'^add_product', add_product, name="add_product"),
    url(r'^add_ingredient_of_product/(?P<product_id>\d+)/', add_ingredient_of_product, name="add_ingredient_of_product"),
    url(r'^add_overhead_of_product/(?P<product_id>\d+)/', add_overhead_of_product, name="add_overhead_of_product"),
    url(r'^product/(?P<product_id>\d+)/edit/', edit_product, name="edit_product")
    # url(r'^index', index, name="index"),
    # url(r'^order', order, name="order"),
    # url(r'^$', product, name="index"),
    # url(r'^(?P<product_id>[0-9]+)$', detail, name="detail"),
    # url(r'^edit/(?P<pk>\d+)$', edit, name="edit"),
]
