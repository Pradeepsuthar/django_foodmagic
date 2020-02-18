from django.shortcuts import render

# Default Seller Home Page
def index(request):
    return render(request, 'seller/index.html')