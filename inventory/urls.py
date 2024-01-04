from django.urls import path
from inventory import views

app_name = 'inventory'
urlpatterns = [
    path('', views.index, name='index'),
    path('inventory/', views.staff_page, name='staff-page'),
]
