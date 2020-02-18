from django.apps import AppConfig


class FoodappConfig(AppConfig):
    name = 'foodapp'
    def ready(self):
        print("="*100)
        from .signals import save_profile