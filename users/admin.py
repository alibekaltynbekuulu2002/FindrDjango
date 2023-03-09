from django.contrib import admin
from .models import User,UserAddress,UserPayment
from django.contrib.auth.admin import UserAdmin

# USER 
class UserAdminConfig(UserAdmin):
    search_fields = ('email','phone_number','first_name','last_name',) # search options
    ordering = ('-created_at',) # ordering options -> shows looking by given param.

    # this is for displaying list of users by showing their fields
    list_display = ('email','phone_number','first_name','last_name','is_active','is_staff','created_at',)

    # filtering options for users
    list_filter = ('email','first_name','last_name','is_active','is_staff',)

    # this are readonly fields these fields are non changible 
    readonly_fields = ('created_at','modified_at')

    # this fieldsets for user model
    fieldsets = ( 
        (None,{'fields':('email','phone_number','first_name','last_name','password')}),
        ('Permissions',{'fields':('is_staff','is_active',)}),
        ('Actions',{'fields':('created_at','modified_at',)}),
    )

    # this fieldsets for adding a new user address
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','phone_number','first_name','last_name','password1','password2',)
        }),
    )

admin.site.register(User,UserAdminConfig)


# USER ADDRESS
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




# USER PAYMENTS
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