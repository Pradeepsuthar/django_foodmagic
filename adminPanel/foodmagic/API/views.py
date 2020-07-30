from rest_framework import viewsets
from core.models import Product, Cetagory, Restaurant
from account.models import Account, Addres
from .serializers import ProductSerializer, CetagorySerializer, RestaurantSerializer, AccountSerializer, AddresSerializer

# Create your views here.

# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CetagoryViewSet(viewsets.ModelViewSet):
    queryset = Cetagory.objects.all()
    serializer_class = CetagorySerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AddresViewSet(viewsets.ModelViewSet):
    queryset = Addres.objects.all()
    serializer_class = AddresSerializer