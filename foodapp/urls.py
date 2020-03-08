from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="HomeApp"),
    path('register/', views.register, name="UserRegistration"),
    path('login/', views.loginUser, name="userLogin"),
    path('logout/', views.logout, name="logout"),   
    path('myaccount/<int:pk>',  views.MyAccount.as_view()), 
    path('products/', views.ProductView),  
    path('search/', views.search, name="search"),
    path('checkout/', views.checkout, name="checkout"),
    path('editprofile/', views.editProfile, name="editprofile"),
    path('changePassword/', views.changePassword, name="changePassword"),
    path('test/', views.test, name="test"),
    path('product_details/', views.productDetails, name="product_details"),
]
