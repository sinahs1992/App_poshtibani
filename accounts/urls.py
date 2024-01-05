from django.urls import path
from accounts.views import CustomStaffLoginView, CustomManagementLoginView
from inventory.views import staff_page
app_name = "accounts"

urlpatterns = [
    path("staff-login/", CustomStaffLoginView.as_view(), name="staff-login"),
    path("management-login/", CustomManagementLoginView.as_view(), name="management-login"),
    path('profile/', staff_page, name='profile'),
]
