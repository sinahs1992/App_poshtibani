from django.contrib import admin
from accounts.models import Staff, WarehouseManager

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass



@admin.register(WarehouseManager)
class WarehouseManagerAdmin(admin.ModelAdmin):
    pass