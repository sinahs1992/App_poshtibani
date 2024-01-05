from django.contrib import admin
from inventory.models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ('device_code', 'staff', 'created_date', 'receip_date')
