from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Profile, Cetagory

# Register your models here.
admin.site.register(Profile)
admin.site.register(Cetagory)
