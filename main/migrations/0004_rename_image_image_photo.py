# Generated by Django 5.0.2 on 2024-04-21 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_items_image2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='Image',
            new_name='Photo',
        ),
    ]