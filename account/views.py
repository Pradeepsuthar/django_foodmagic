from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from .models import Account
from django.contrib.sessions.models import Session
from random import randint
otp = 0

# Create your views here.
def login(request):
    if request.method == 'POST':
        mobile = request.POST['mobile_number']
        password = request.POST['password']
        user = auth.authenticate(mobile=mobile, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['is_login'] = True
            print("Loged in")

            if request.session.has_key('is_login'):
                return redirect('/home/')
            else:
                return redirect('/')
        else:
            print("Loged in faild")
            return redirect('/')
    return render(request, 'login.html',{'title':'Order online food on foodMagic'})

# Create new user
def signUp(request):
    title = 'Order online food on foodMagic'
    # Get data from user
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile_number = request.POST['mobile_number']
        email = request.POST['email']
        password = request.POST['password']
        get_otp = randint(999,9999)
        global otp
        otp = get_otp
        print("Your OTP is ",otp)
        
        if Account.objects.filter(email=email).exists():
            print("Email is already taken...")
            return redirect('/')
        elif Account.objects.filter(mobile=mobile_number).exists():
            print("Mobile number is already exits")
            return redirect('/')
        else:
            user = Account.objects.create_user(mobile=mobile_number,first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            print("Registration Successfully")
            return redirect('/verify/')
    else:
        return render(request, 'signup.html',{'title':title})

# Mobile number verification
def verifyMobile(request):
    title = 'Verifying mobile number'
    if request.method == 'POST':   
        get_user_otp = request.POST['otp']
        if otp == int(get_user_otp):
            return redirect('/home/')
        else:
            not_verify = 'Your OTP is wrong please check again'
            return render(request, 'verify.html', {'title':title,'wrong_otp':not_verify})
    else:    
        return render(request, 'verify.html', {'title':title})
    

# Logout user from dashboard
def logout(request):
    if request.session.has_key('is_login'):
        auth.logout(request)
        return redirect('/')
    else:
        return redirect('/')