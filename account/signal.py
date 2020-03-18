from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from time import strftime
from .models import Account, Addres

@receiver(post_save, sender=Account)
def save_Addres(sender, instance, created, **kwarg):
    if created:
        Addres.objects.create(user=instance)
