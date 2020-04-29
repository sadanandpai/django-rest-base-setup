from django.contrib import admin
from django.contrib.auth.models import Permission

# Register your models here.
class PermissionAdmin(admin.ModelAdmin):
    model = Permission
    fields = ['name']

# Register your models here.
admin.site.register(Permission, PermissionAdmin)