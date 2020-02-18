from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="HomeApp"),
    path('register/', views.register, name="UserRegistration"),
    path('login/', views.loginUser, name="userLogin"),
    path('menu/', views.home, name="home"),
    path('logout/', views.logout, name="logout"),   
    path('myaccount/<int:pk>',  views.MyAccount.as_view()),   
]
