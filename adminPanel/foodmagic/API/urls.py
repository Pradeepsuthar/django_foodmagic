from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'restaurant', views.RestaurantViewSet)
router.register(r'cetagory', views.CetagoryViewSet)
router.register(r'accounts', views.AccountViewSet)
router.register(r'address', views.AddresViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]