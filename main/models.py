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


class Contact(models.Model):
    phone_number = models.CharField(max_length=55)
    email = models.CharField(max_length=155)
    location = models.CharField(max_length=255)


class ShopBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shopbanner/')

    def save(self, *args, **kwargs):
        super(ShopBanner, self).save(*args, **kwargs)
        self.process_image()

    def process_image(self):
        try:
            # Open the image
            img = Image.open(self.image.path)

            # Check if the image dimensions are within the specified range
            width, height = img.size
            if width < 1920 or height < 1080:
                # Resize the image to fit within the specified range while maintaining aspect ratio
                img.thumbnail((1920, 1080))
                img.save(self.image.path)  # Overwrite the original image with the resized one

            elif width > 300 or height > 300:
                # Resize the image to fit within the specified range while maintaining aspect ratio
                img.thumbnail((300, 300))
                img.save(self.image.path)  # Overwrite the original image with the resized one

            # Optionally return the processed image or just confirm it's processed
            return "Image processed successfully."

        except IOError:
            return "Unable to process image. Please check the file path or format."


class AboutBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shopbanner/')

    def save(self, *args, **kwargs):
        super(ShopBanner, self).save(*args, **kwargs)
        self.process_image()

    def process_image(self):
        try:
            # Open the image
            img = Image.open(self.image.path)

            # Check if the image dimensions are within the specified range
            width, height = img.size
            if width < 1920 or height < 1080:
                # Resize the image to fit within the specified range while maintaining aspect ratio
                img.thumbnail((1920, 1080))
                img.save(self.image.path)  # Overwrite the original image with the resized one

            elif width > 300 or height > 300:
                # Resize the image to fit within the specified range while maintaining aspect ratio
                img.thumbnail((300, 300))
                img.save(self.image.path)  # Overwrite the original image with the resized one

            # Optionally return the processed image or just confirm it's processed
            return "Image processed successfully."

        except IOError:
            return "Unable to process image. Please check the file path or format."


class BlogBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shopbanner/')



class ContactBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shopbanner/')

    def save(self, *args, **kwargs):
        super(ShopBanner, self).save(*args, **kwargs)
        self.process_image()

    def process_image(self):
        try:
            # Open the image
            img = Image.open(self.image.path)

            # Check if the image dimensions are within the specified range
            width, height = img.size
            if width < 1920 or height < 1080:
                # Resize the image to fit within the specified range while maintaining aspect ratio
                img.thumbnail((1920, 1080))
                img.save(self.image.path)  # Overwrite the original image with the resized one

            elif width > 300 or height > 300:
                # Resize the image to fit within the specified range while maintaining aspect ratio
                img.thumbnail((300, 300))
                img.save(self.image.path)  # Overwrite the original image with the resized one

            # Optionally return the processed image or just confirm it's processed
            return "Image processed successfully."

        except IOError:
            return "Unable to process image. Please check the file path or format."