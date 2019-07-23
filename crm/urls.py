from django.conf.urls import url

from . import views

app_name = "crm"

urlpatterns = [
    # url(r'^$', views.customer, name='customer'),
    url('customer', views.customer, name='customer'),
    url('providers/', views.provider, name='provider'),
    url('product/', views.product, name='product'),
    url('deal/', views.deal, name='deal'),
]