from django.contrib import admin
from accounts.models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass
