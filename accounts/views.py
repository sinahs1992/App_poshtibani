from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import messages
from django.shortcuts import redirect

class CustomStaffLoginView(LoginView):
    template_name = 'accounts/staff_login.html'
    # success_url = reverse('inventory:staff-page')


    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # Redirect to a different page if the user is already logged in
            return redirect('inventory:staff-page')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "You have been successfully logged in!")
        return response

    def get_success_url(self):
        # Customize the success URL dynamically here based on user or other conditions
        return reverse('inventory:staff-page')
    

class CustomManagementLoginView(LoginView):
    template_name = 'accounts/management_login.html'
    # success_url = reverse('inventory:staff-page')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # Redirect to a different page if the user is already logged in
            return redirect('management:management-select-page')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "You have been successfully logged in!")
        return response

    def get_success_url(self):
        # Customize the success URL dynamically here based on user or other conditions
        return reverse('management:management-select-page')