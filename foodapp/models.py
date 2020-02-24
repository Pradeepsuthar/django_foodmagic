from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete = CASCADE)
    profile_img = models.ImageField(upload_to = "images\\userProfiles\\", null=True)
    phone_no = models.CharField(default="",validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=10)
    current_address = models.CharField(default="", max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s" % self.user

class Cetagory(models.Model):
    cetagory_name = models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.cetagory_name)

class Restaurant(models.Model):
    restaurant_img = models.ImageField(upload_to = "images\\restaurants-img\\", null=True)
    restaurant_name = models.CharField(max_length=400)
    restaurant_address = models.CharField(default="", max_length=100)
    restaurant_owner =  models.OneToOneField(to=User, on_delete = CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)
    restaurant_owner_phone_no = models.CharField(default="",validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=10)
    def __str__(self):
        return "%s" % (self.restaurant_name)

class Product(models.Model):
    product_img = models.ImageField(upload_to = "images\\product-img\\", null=True)
    product_name = models.CharField(max_length=300)
    price = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(1000)])
    product_dec = models.TextField(null=True, blank=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(null=True, blank=True,max_length=100)
    cetagory = models.ForeignKey(to=Cetagory, on_delete = CASCADE, null=True, blank=True)
    restaurant_name = models.ForeignKey(to=Restaurant, on_delete = CASCADE, null=True, blank=True)
    is_veg = models.BooleanField(default=True)
    def __str__(self):
        return "%s" % (self.product_name)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    customer_name = models.CharField(max_length=90)
    customer_email = models.CharField(max_length=111)
    customer_address = models.CharField(default="", max_length=100)
    customer_city = models.CharField(max_length=111)
    customer_state = models.CharField(max_length=111)
    customer_pin_code = models.CharField(max_length=111)
    payment_method = models.CharField(default="Case on Delivery",max_length=111)
    cr_date = models.DateTimeField(auto_now_add=True)
    customer_phone = models.CharField(default="",validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=10)