from django.urls import path
from management import views
handler403 = views.permission_denied_view
app_name = 'management'


urlpatterns = [
    path('', views.management_select_page, name='management-select-page'),
    path('allocation/', views.allocation_page, name='allocation-page'),
    path('inventory/', views.inventory_page, name='inventory-page'),
    path('inventory/recepted/<str:device_code>/', views.recepted, name="recepted"),
    path('inventory/installed/<str:device_code>/', views.installed, name="installed"),
]

