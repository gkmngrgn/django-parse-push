from django.contrib import admin
from django_parse_push.models import Device


class DeviceAdmin(admin.ModelAdmin):
    list_display = ("device_id", "device_type", "user", "is_active", "created_at")


admin.site.register(Device, DeviceAdmin)
