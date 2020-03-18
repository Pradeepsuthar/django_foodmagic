from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home_Page'),
    path('profile/', views.userProfile, name='profile'),
    path('search/', views.search, name='search'),
    path('settings/', views.userSetting, name='settings'),
    path('veg/', views.vegItems, name='veg'),
    path('non-veg/', views.nonVegItems, name='non-veg'),
    path('recommended/', views.Recommendation, name='non-veg'),
    path('help/', views.helpSection, name='help'),
    path('changeaddress/', views.updateAddress, name='changeaddress'),
] 