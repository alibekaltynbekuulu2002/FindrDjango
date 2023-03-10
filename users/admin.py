from django.contrib import admin
from .models import User,UserAddress,UserPayment
from django.contrib.auth.admin import UserAdmin

"""
USER
"""
class UserAdminConfig(UserAdmin):
    search_fields = ('email','phone_number','first_name','last_name',)
    ordering = ('created_at',)
    list_display = ('email','phone_number','first_name','last_name','is_active','is_staff','created_at',)
    list_filter = ('email','first_name','last_name','is_active','is_staff',)
    readonly_fields = ('created_at','modified_at','is_superuser')
    fieldsets = ( 
        (None,{'fields':('email','phone_number','first_name','last_name','password')}),
        ('Permissions',{'fields':('is_staff','is_active','is_superuser')}),
        ('Actions',{'fields':('created_at','modified_at',)}),
        ('Groups',{'fields':('groups',)})
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','phone_number','first_name','last_name','password1','password2',)
        }),
    )

admin.site.register(User,UserAdminConfig)


"""
USER ADDRESS
"""
class UserAddressAdminConfig(admin.ModelAdmin):
    search_fields = ('country','city','address_line1','address_line2','postal_code',)
    ordering = ('-country',)
    list_display = ('country','city','address_line1','address_line2','postal_code','user',)
    list_filter = ('country','city','address_line1','address_line2','postal_code',)
    fieldsets = ( 
        (None,{'fields':('country','city','address_line1','address_line2','postal_code','user')}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('address_line1','address_line2','user','country','city','postal_code',)
        }),
    )

admin.site.register(UserAddress,UserAddressAdminConfig)



"""
USER PAYMENT
"""
class UserPaymentAdminConfig(admin.ModelAdmin):
    search_fields = ('user','payment_type','provider','account_no','expiry',)
    ordering = ('-user',)
    list_display = ('user','payment_type','provider','account_no','expiry',)
    list_filter = ('payment_type','provider','account_no','expiry',)
    fieldsets = ( 
        (None,{'fields':('user','payment_type','provider','account_no','expiry',)}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('user','payment_type','provider','account_no','expiry',)
        }),
    )
    
admin.site.register(UserPayment,UserPaymentAdminConfig)

