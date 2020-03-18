from django.shortcuts import render, redirect
from .models import Product, Cetagory, Restaurant
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from account.models import Account, Addres

import requests 

# Create your views here.
@login_required(login_url='/')
def index(request):
    title = 'FoodMagic'
    products = Product.objects.order_by("?")
    all_cetagories = Cetagory.objects.order_by("?")
    all_veg = Product.objects.all_veg_products()
    all_nonveg = Product.objects.all_nonveg_products()
    return render(request, 'index.html', {'title':title,'products':products,'all_cetagories':all_cetagories,'all_veg_products':all_veg,'all_nonveg_products':all_nonveg})

# Search
@login_required(login_url='/')
def search(request):
    title = 'Search'
    search_item = request.GET.get('search')
    if search_item == None and len(search_item) > 50:
        search_item = Product.objects.none()
    Cetagory_list = Cetagory.objects.all()
    products = Product.objects.filter(product_name__icontains = search_item.strip())
    return render(request, 'search.html',{'title':title,'all_cetagories':Cetagory_list,'products':products,'search':search_item})

@login_required(login_url='/')
def userSetting(request):
    title = 'Settings'
    return render(request, 'settings.html', {'title':title})

@login_required(login_url='/')
def vegItems(request):
    title = 'Only Veg Items'
    all_veg = Product.objects.all_veg_products().order_by('?')
    return render(request, 'veg-items.html', {'title':title,'all_veg_products':all_veg})

@login_required(login_url='/')
def nonVegItems(request):
    title = 'Only Non-Veg Items'
    all_nonveg = Product.objects.all_nonveg_products().order_by('?')
    return render(request, 'non-veg-tems.html', {'title':title,'all_nonveg_products':all_nonveg})

@login_required(login_url='/')
def Recommendation(request):
    title = 'Recommendation'

    r = requests.get('http://127.0.0.1:8000/api/restaurant/') 
    # extracting data in json format 
    data = r.json() 

    for i in data:
        url = i['restaurant_img']

    
    # img = data['restaurant_img']

    return render(request, 'recommendation.html',{'title':title,'api_data':data,'url':url})

@login_required(login_url='/')
def userProfile(request):
    title = 'Profile'
    if request.user.is_authenticated:
        address = Addres.objects.all().filter(user=request.user)
    else:
        pass
    return render(request, 'profile.html',{'title':title,'address':address})

@login_required(login_url='/')
def helpSection(request):
    title = 'Help'
    return render(request, 'help.html',{'title':title})


@login_required(login_url='/')
def updateAddress(request):
    if request.method == 'POST':
        area = request.POST.get('area')
        district = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        if request.user.is_authenticated:
            address = Addres.objects.all().get(user=request.user)
            address.area = area
            address.district = district
            address.state = state
            address.pincode = pincode
            address.save()
            return redirect('/home/profile/')
        else:
            pass



