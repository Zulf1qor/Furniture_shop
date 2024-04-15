from django.urls import path
from .views import *

urlpatterns = [
    path('',index_view, name='index_url'),
    path('shop',shop_view, name='shop_url'),
    path('about', about_view, name='about_url'),
    path('blog',blog_view, name='blog_url'),
    path('blog-detail', blog_detail_view, name="blog-detail_url"),
    path('contact', contact_view, name='contact_url'),
    path('cart', cart_view, name='cart_url'),
    path('login', login_view, name='login_url'),
    path('my-account', my_account, name='my_account_url'),
    path('wishlist', wishlist_view, name='wishlist_url'),
    path('create_comment/<int:pk>/', create_comment, name='create_comment_url')

]