from django.shortcuts import render
from .models import *

def index_view(request):
    return render(request,'index.html')

def shop_view(request):
    return render(request,'shop.html')

def about_view(request):
    return render(request,'about.html')

def blog_view(request):
    context = {
        'blog': Blog.objects.all().order_by('-id')[:6],
        'blogbanner':BlogBanner.objects.last()
    }
    return render(request, 'blog.html', context)

def blog_detail_view(request):
    context = {
        'blogdetails': Details.objects.last(),
        'blogbanner':BlogBanner.objects.last()

    }
    return render(request, "blog-details.html", context)

def contact_view(request):
    return render(request,'contact.html')

def cart_view(request):
    return render(request,'cart.html')

def login_view(request):
    return render(request,'login.html')

def my_account(request):
    return render(request,'my-account.html')

def wishlist_view(request):
    return render(request,'wishlist.html')
