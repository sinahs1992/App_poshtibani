from django.urls import path
from accounts.views import CustomLoginView
from inventory.views import staff_page
app_name = "accounts"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="staff-login"),
    path('profile/', staff_page, name='profile'),
]
