from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,phone_number,email,first_name,last_name,password,**extra_fields):
        if not phone_number:
            raise ValueError(_('The phone number field must be set'))
        if not email:
            raise ValueError(_('The email field must be set'))
        if not first_name:
            raise ValueError(_('The first name field must be set'))
        if not last_name:
            raise ValueError(_('The last name field must be set'))
        
        email = self.normalize_email(email)
        user = self.model(
            phone_number=phone_number,email=email,
            first_name=first_name,last_name=last_name,
            **extra_fields)
            
        user.set_password(password)
        user.save()
        return user
        

    def create_superuser(self,phone_number,email,first_name,last_name,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('The superuser must be assigned to is_staff = True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('The superuser must be assigned to is_superuser = True.'))

        return self.create_user(phone_number,email,first_name,last_name,password,**extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    MALE = 'MALE'
    FEMALE = 'FEMALE'

    GENDER_CHOICES = [
        (MALE,'M'),
        (FEMALE,'F')
    ]

    phone_number = models.CharField(_('phone number'),unique=True,max_length=30)
    email = models.EmailField(_('email address'),unique=True,max_length=255,null=True,blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,null=True,default=None)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email','first_name','last_name']

    def __str__(self) -> str:
        return f'{self.phone_number} : {self.first_name} {self.last_name}'

    class Meta:
        db_table = 'users'




class UserAddress(models.Model):
    user = models.ForeignKey(User,related_name='address',on_delete=models.CASCADE)
    address_line1 = models.CharField(_('Address Line 1'),max_length=100)
    address_line2 = models.CharField(_('Address Line 2'),max_length=100,null=True,blank=True)
    city = models.CharField(_('City'),max_length=50,default='Bishkek')
    country = models.CharField(_('Country'),max_length=50,default='Kyrgyzstan')
    postal_code = models.CharField(_('Postal Code'),max_length=50,default='720000')

    def __str__(self) -> str:
        return f'{self.country} / {self.city} / {self.address_line1}'
    
    class Meta:
        db_table = 'user_addresses'
    


class UserPayment(models.Model):
    VISA = 'Visa'
    CASH = 'Cash'
    PAYMENT_TYPE_CHOICES = [
        (VISA,'Visa'),
        (CASH,'Cash')
    ]

    user = models.ForeignKey(User,related_name='payment',on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20,choices=PAYMENT_TYPE_CHOICES,default=CASH)
    provider = models.CharField(max_length=50,null=True,blank=True)
    account_no = models.CharField(max_length=50,null=True,blank=True)
    expiry = models.CharField(max_length=10,null=True,blank=True)


    def __str__(self) -> str:
        return f'{self.user} : {self.payment_type} {self.provider} {self.account_no} {self.expiry}'
    

    class Meta:
        db_table = 'user_payments'

