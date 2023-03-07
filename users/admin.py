from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserAdminConfig(UserAdmin):
    search_fields = ('email','phone_number','first_name','last_name',)
    ordering = ('-created_at',)
    list_display = ('email','phone_number','first_name','last_name','is_active','is_staff','created_at',)
    list_filter = ('email','first_name','last_name','is_active','is_staff',)
    readonly_fields = ('created_at','modified_at')
    fieldsets = (
        (None,{'fields':('email','phone_number','first_name','last_name',)}),
        ('Permissions',{'fields':('is_staff','is_active',)}),
        ('Actions',{'fields':('created_at','modified_at',)}),
    )



admin.site.register(User,UserAdminConfig)