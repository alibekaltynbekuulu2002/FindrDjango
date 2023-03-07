from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
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



# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    phone_number = models.CharField(_('phone number'),unique=True,max_length=30)
    email = models.EmailField(_('email address'),unique=True,max_length=255,null=True,blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email','first_name','last_name']

    def __str__(self) -> str:
        return f'{self.phone_number} : {self.first_name} {self.last_name}'

    class Meta:
        db_table = 'users'