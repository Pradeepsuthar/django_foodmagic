from django.contrib import admin
from .models import Cetagory, Product, Restaurant
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class ProductAdmin(ModelAdmin):
    list_display = ["id","product_name", "cetagory", "price","food_preparation_time","restaurant_name","is_veg","cr_date"]
    search_fields = ["product_name", "cetagory"]
    list_filter = ["cr_date"]
admin.site.register(Product, ProductAdmin)

admin.site.register(Cetagory)

class RestaurantAdmin(ModelAdmin):
    list_display = ["id","restaurant_name", "restaurant_owner", "restaurant_owner_phone_no","mini_order_price", "restaurant_address", "cr_date"]
    search_fields = ["restaurant_name", "restaurant_address"]
    list_filter = ["cr_date"]
admin.site.register(Restaurant, RestaurantAdmin)