# Generated by Django 5.0.2 on 2024-04-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_items_old_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='image2',
            field=models.ImageField(default=1, upload_to='items_photo2/'),
            preserve_default=False,
        ),
    ]
