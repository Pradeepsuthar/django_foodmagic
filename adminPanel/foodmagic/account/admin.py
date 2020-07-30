from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Account, Addres

# Register your models here.
class AccountAdmin(ModelAdmin):
    list_display = ["id","first_name", "last_name", "email","mobile","date_joined","is_admin","is_active","last_login"]
    search_fields = ["id","first_name", "last_name","mobile"]
    readonly_fields = ["date_joined","last_login","is_admin","is_superuser","is_staff","is_active"]
admin.site.register(Account, AccountAdmin)

class AddresAdmin(ModelAdmin):
    list_display = ["id","user", "area","district","state", "pincode", "cr_date"]
    search_fields = ["area","district","state", "pincode"]
    list_filter = ["cr_date"]
admin.site.register(Addres, AddresAdmin)

