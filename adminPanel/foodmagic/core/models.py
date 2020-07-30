from django.db import models
from django.db.models import Model, Manager
from account.models import Account
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# Create your models here.
class Restaurant(models.Model):
    restaurant_img = models.ImageField(upload_to = "images\\restaurants-img\\", null=True)
    restaurant_name = models.CharField(max_length=400)
    restaurant_address = models.CharField(default="", max_length=100)
    restaurant_owner =  models.OneToOneField(to=Account, on_delete = CASCADE)
    restaurant_owner_phone_no = models.CharField(default="",validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=10)
    mini_order_price = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(10000)])
    cr_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s" % (self.restaurant_name)

class Cetagory(models.Model):
    cetagory_name = models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.cetagory_name)

class ProductManager(models.Manager):
    def search_product(self, keyword):
        return self.filter(product_name__icontains=keyword)

    def get_queryset(self):
        return super().get_queryset()
    
    def all_veg_products(self):
        return super().get_queryset().filter(is_veg=True)

    def all_nonveg_products(self):
        return super().get_queryset().filter(is_veg=False)

    def all_veg_products(self):
        return super().get_queryset().filter(is_veg=True)

class Product(models.Model):
    product_img = models.ImageField(upload_to = "images\\product-img\\", null=True)
    product_name = models.CharField(max_length=300)
    price = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(10000)])
    food_preparation_time = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(1000)])
    cetagory = models.ForeignKey(to=Cetagory, on_delete = CASCADE, null=True, blank=True)
    restaurant_name = models.ForeignKey(to=Restaurant, on_delete = CASCADE, null=True, blank=True)
    is_veg = models.BooleanField(default=True)
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % (self.product_name)

    objects = ProductManager()


