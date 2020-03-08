from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Profile, Cetagory, Product, Restaurant, Order
from django.contrib.sessions.models import Session
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Default Home Page
def index(request):
    return redirect('/products/')

# Testing page
def test(request):
    return render(request, 'test/test.html')

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
            return redirect('/products/')
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


# MyAccount
class MyAccount(TemplateView):
    template_name = "myaccount.html"
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context["profile"] = Profile.objects.all()
        return context


# Product view
@login_required(login_url='/login/')
def ProductView(request):
    if request.session.has_key('is_login'):
        products = Product.objects.order_by("?")
        all_cetagories = Cetagory.objects.order_by("?")
        return render(request, 'foodProduct/products.html',{'products':products,'all_cetagories':all_cetagories})
    else:
        return redirect('/login/')



# Product Detail view
@login_required(login_url='/login/')
def productDetails(request):
    if request.session.has_key('is_login'):
        products = Product.objects.order_by("?")
        all_cetagories = Cetagory.objects.order_by("?")
        return render(request, 'foodProduct/productDetails.html',{'products':products,'all_cetagories':all_cetagories})
    else:
        return redirect('/login/')    


# Search
@login_required(login_url='/login/')
def search(request):
    if request.session.has_key('is_login'):
        search_item = request.GET.get('search')
        if search_item == None and len(search_item) > 50:
            search_item = Product.objects.none()
        Cetagory_list = Cetagory.objects.all()
        products = Product.objects.filter(product_name__icontains = search_item)
        if request.session.has_key('is_login'):
            return render(request, 'foodProduct/products.html',{'all_cetagories':Cetagory_list,'products':products,'search':search_item})
        else:
            return redirect('/login/')
    else:
        return redirect('/login/')


# Checkout
@login_required(login_url='/login/')
def checkout(request):
    if request.session.has_key('is_login'):
        if request.method=="POST":
            items_json = request.POST.get('myJSON', '')
            print("My json data is : ",items_json)
            name = request.POST.get('fname', '') + " " + request.POST.get('lname', '')
            email = request.POST.get('email', '')
            address = request.POST.get('address', '')
            city = request.POST.get('city', '')
            state = request.POST.get('state', '')
            pin_code = request.POST.get('pin_code', '')
            payment_method = request.POST.get('paymentMethod', '')
            phone = request.POST.get('phone_no', '')
            order = Order(items_json=items_json, customer_name=name, customer_email=email, customer_address=address, customer_city=city,
                        customer_state=state, customer_pin_code=pin_code, payment_method=payment_method, customer_phone=phone)
            order.save()
            order_placed = True
            order_id = order.order_id
            return render(request, 'foodProduct/checkout.html', {'order_placed':order_placed, 'order_id': order_id})
        else:
            return render(request, 'foodProduct/checkout.html')
    else:
        return redirect('/login/')


# Edit Profile
@login_required(login_url='/login/')
def editProfile(request):
    if request.session.has_key('is_login'):
        if request.method=='POST':
            current_user = request.POST.get('username', '')
            # profile_img = request.POST.get('profile_img', '')
            fname = request.POST.get('edit_fname', '')
            lname = request.POST.get('edit_lname', '')
            phone_no = request.POST.get('edit_phone_no', '')
            email = request.POST.get('edit_email', '')
            current_address = request.POST.get('edit_current_address', '')
            user = User.objects.get(username=current_user)
            profile = Profile.objects.all()
            user.first_name = fname
            user.last_name = lname
            user.email = email
            # user.profile.profile_img = profile_img
            user.profile.phone_no = phone_no
            user.profile.current_address = current_address
            user.save()
            user.profile.save()   
            # print("src : ",user.profile.profile_img.url) 
            # print("img :",profile_img)    
            return render(request, 'myaccount.html')
    else:
        return redirect('/login/')
    

# Change Password
@login_required(login_url='/login/')
def changePassword(request):
    if request.session.has_key('is_login'):
        if request.method=='POST':
            current_user = request.user
            current_pass = request.POST.get('cpass', '')
            pass1 = request.POST.get('pass1', '')
            pass2 = request.POST.get('pass2', '')
            user = User.objects.get(username=current_user)
            if pass1 == pass2:
                newPass = pass1
                user.set_password(newPass)
                user.save() # call save explicitly
                messages.success(request, 'Your password is change')
                return redirect('/login/')
            else:
                messages.info(request, 'Your password and confrim password are not match.')

            return render(request, 'myaccount.html')
    else:
        return redirect('/login/')


# Logout user from dashboard
@login_required(login_url='/login/')
def logout(request):
    if request.session.has_key('is_login'):
        auth.logout(request)
        return redirect('/login/')
    else:
        return redirect('/login/')