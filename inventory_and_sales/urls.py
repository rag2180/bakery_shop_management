from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^products', products, name="products"),
    url(r'^(?P<pk>\d+)$', detail, name="detail"),
    url(r'^add_product$', add_product, name="add_product"),
    # url(r'^index', index, name="index"),
    # url(r'^order', order, name="order"),
    # url(r'^$', product, name="index"),
    # url(r'^(?P<product_id>[0-9]+)$', detail, name="detail"),
    # url(r'^edit/(?P<pk>\d+)$', edit, name="edit"),
]
