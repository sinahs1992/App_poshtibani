from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import messages


class CustomLoginView(LoginView):
    template_name = 'accounts/staff_login.html'
    # success_url = reverse('inventory:staff-page')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "You have been successfully logged in!")
        return response

    def get_success_url(self):
        # Customize the success URL dynamically here based on user or other conditions
        return reverse('inventory:staff-page')