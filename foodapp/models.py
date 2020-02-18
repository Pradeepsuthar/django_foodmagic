from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete = CASCADE)
    profile_img = models.ImageField(upload_to = "images\\userProfiles\\", null=True)
    phone_no = models.CharField(default="9876543210",validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=10)
    current_address = models.CharField(default="Current Address", max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s" % self.user

class Cetagory(models.Model):
    cetagory_name = models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.cetagory_name)