from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Profile, Cetagory, Product, Restaurant, Order
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_select_related = ('profile', )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class ProductAdmin(ModelAdmin):
    list_display = ["product_name", "cetagory", "price", "created_by", "cr_date"]
    search_fields = ["product_name", "cetagory"]
    list_filter = ["cr_date"]
admin.site.register(Product, ProductAdmin)

admin.site.register(Cetagory)

class RestaurantAdmin(ModelAdmin):
    list_display = ["restaurant_name", "restaurant_owner", "restaurant_owner_phone_no", "restaurant_address", "cr_date"]
    search_fields = ["restaurant_name", "restaurant_address"]
    list_filter = ["cr_date"]
admin.site.register(Restaurant, RestaurantAdmin)

class OrderAdmin(ModelAdmin):
    list_display = ["order_id", "customer_name", "customer_phone", "customer_address", "customer_city", "customer_pin_code", "payment_method", "cr_date"]
    search_fields = ["order_id", "customer_name", "cr_date", "customer_city"]
    list_filter = ["cr_date"]
admin.site.register(Order, OrderAdmin)




