from django.urls import path
from . import views

app_name = 'erp'

urlpatterns = [
    path('', views.home, name='home'),
    path('erp/', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
]