from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='Login_Page'),
    path('signUp/', views.signUp, name='SignUp_Page'),
    path('verify/',views.verifyMobile, name='mobileVerification'),
    path('logout/',views.logout, name='logout'),
    path('home/', include('core.urls'), name='home'),
] 