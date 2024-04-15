from django.db import models
from PIL import Image

class Banner(models.Model):
    title1 = models.CharField(max_length=155)
    title2 = models.CharField(max_length=155)
    title3 = models.CharField(max_length=155)
    image = models.ImageField(upload_to='banner_photo/')

class Furniture(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='furtinure_photo/')


class Items(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='items_photo/')
    old_price = models.DecimalField(decimal_places=2, max_digits=10)
    new_price = models.DecimalField(decimal_places=2, max_digits=10)


class Image(models.Model):
    Image = models.ImageField(upload_to='Image/')


class About(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='about_photo/')
    image2 = models.ImageField(upload_to='about_photo2/')


class Brand(models.Model):
    logo = models.ImageField(upload_to='brand_logo/')


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_image/')


class Blog(models.Model):
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Blog_image/')
    date = models.DateTimeField(auto_now=True)


class Details(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Details_photo/')
    title = models.CharField(max_length=255)
    text = models.TextField()
    description = models.CharField(max_length=255)


class Comment(models.Model):
    name = models.CharField(max_length=55)
    data = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=255)


class Contact(models.Model):
    phone_number = models.CharField(max_length=55)
    email = models.CharField(max_length=155)
    location = models.CharField(max_length=255)


class ShopBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shopbanner/')


class AboutBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shopbanner/')


class BlogBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shopbanner/')



class ContactBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shopbanner/')

