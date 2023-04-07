from django.urls import path
from . import views

app_name = 'erp'

urlpatterns = [
    path('', views.home, name='home'),
    path('erp/', views.product_list, name='product_list'),
    path('erp/create/', views.product_create, name='product_create'),
    path('erp/inbound/<int:product_id>', views.inbound_create, name='inbound_create'),
    path('erp/outbound/<int:product_id>', views.outbound_create, name='outbound_create'),
    path('erp/inventory/<int:product_id>', views.inventory, name='product_inventory'),
]