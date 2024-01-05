from django.urls import path
from management import views

app_name = 'management'

urlpatterns = [
    path('', views.management_select_page, name='management-select-page'),
    path('allocation/', views.allocation_page, name='allocation-page'),
    path('inventory/', views.inventory_page, name='inventory-page'),
]
