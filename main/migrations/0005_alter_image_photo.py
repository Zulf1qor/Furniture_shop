# Generated by Django 5.0.2 on 2024-04-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_image_image_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='Photo',
            field=models.ImageField(upload_to='Image1/'),
        ),
    ]
