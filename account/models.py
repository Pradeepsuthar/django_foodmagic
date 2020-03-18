from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db.models import Model, Manager

# Create your models here.
class MyAccountManager(BaseUserManager):
    
    def create_user(self, email, mobile, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not mobile:
            raise ValueError("Users must have a mobile number")

        user = self.model(
            email = self.normalize_email(email),
            mobile = mobile,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            mobile = mobile,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name='email',max_length=60, unique=True)
    mobile = models.CharField(default="",validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=10, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    def __str__(self):
        return self.first_name +" "+ self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Addres(models.Model):
    user = models.OneToOneField(to=Account, on_delete=CASCADE)
    area = models.CharField(default="Geetanjali Institute of Technical Studies, Dabok",max_length=400)
    pincode = models.CharField(default="303122", max_length=6)
    district = models.CharField(default="Udaipur", max_length=100)
    state = models.CharField(default="Rajasthan", max_length=100)
    cr_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s" % (self.area)
