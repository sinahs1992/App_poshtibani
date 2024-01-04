from django.contrib import admin
from inventory.models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass
