from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="HomeApp"),
    path('register/', views.register, name="UserRegistration"),
    path('login/', views.loginUser, name="userLogin"),
    path('menu/', views.home, name="home"),
    path('logout/', views.logout, name="logout"),   
    path('myaccount/<int:pk>',  views.MyAccount.as_view()), 
    path('products/', views.ProductView.as_view()),  
    path('search/', views.search, name="search"),
    path('checkout/', views.checkout, name="checkout"),
    path('editprofile/', views.editProfile, name="editprofile"),
    path('changePassword/', views.changePassword, name="changePassword"),
]
