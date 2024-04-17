from django.shortcuts import render,redirect
from .models import *

def index_view(request):
    return render(request,'index.html')

def shop_view(request):
    return render(request,'shop.html')

def about_view(request):
    context = {
        'aboutbanner':AboutBanner.objects.last()
    }
    return render(request,'about.html')

def blog_view(request):
    context = {
        'blog': Blog.objects.all().order_by('-id')[:6],
        'blogbanner':BlogBanner.objects.last()
    }
    return render(request, 'blog.html', context)

def blog_detail_view(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog':blog,
        'blogdetails': Details.objects.last(),
        'blogbanner':BlogBanner.objects.last(),
        'category':Category.objects.all().order_by('-id')[:5],
        'furniture':Furniture.objects.all().order_by('-id')[:3],
        'comment':Comment.objects.all().order_by('-id')[:3]

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


def create_comment_view(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == "POST":
        comment = request.POST['comment']
        name = request.POST['name']
        Comment.objects.create(
            name = name,
            comment = comment,

        )
        return redirect('blog-detail_url', blog.id)

