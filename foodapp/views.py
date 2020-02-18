from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Profile, Cetagory
from django.contrib.sessions.models import Session
from django.views.generic import TemplateView

# Default Home Page
def index(request):
    if request.session.has_key('is_login'):
        return redirect('/menu/')
    else:
        return render(request, 'index.html')

# Login exists user  
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            request.session['is_login'] = True
            auth.login(request, user)
            print("Loged in")
            return redirect('/menu/')
        else:
            messages.info(request, 'Invalid Username and Password! Please try again.')
            print("Loged in faild")
            return redirect('/login/')
    else:
        return render(request, 'login.html')
        
# Register new user           
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("Username is already taken...")
                messages.error(request, 'Username is already taken!!! Please try again...')
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                print("Email is already taken...")
                messages.error(request, 'Email is already taken!!! Please try again...')
                return redirect('/register/')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save()
                print("Registration Successfully")
                messages.success(request, 'Registration Successfully! Now you can login.')
                return redirect('/login/')
        else:
            print("Password and Confrim password are not same please try again")
            messages.error(request, 'Password and Confrim password are not same please try again')
        return redirect('/register/')
    else:
        return render(request, 'register.html')

# Dashboard for authenticated users
def home(request):
    Cetagory_list = Cetagory.objects.all()
    if request.session.has_key('is_login'):
        return render(request, 'home.html',{'all_cetagories':Cetagory_list})
    else:
        return redirect('/login/')

# Logout user from dashboard
def logout(request):
    auth.logout(request)
    return redirect('/')

class MyAccount(TemplateView):
    template_name = "myaccount.html"
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context["profile"] = Profile.objects.all()
        return context