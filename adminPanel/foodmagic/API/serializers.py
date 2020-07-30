from rest_framework import serializers
from core.models import Product, Cetagory, Restaurant
from account.models import Account, Addres

# Serializers define the API representation.
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CetagorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cetagory
        fields = '__all__'

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['id','email' ,'mobile','is_staff']

class AddresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Addres
        fields = '__all__'



