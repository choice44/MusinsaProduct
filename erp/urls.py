from django.urls import path
from . import views

app_name = 'erp'

urlpatterns = [
    path('', views.home, name='home'),
    path('erp/', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('inbound/<int:product_id>', views.inbound_create, name='inbound_create'),
    path('outbound/<int:product_id>', views.outbound_create, name='outbound_create'),
]