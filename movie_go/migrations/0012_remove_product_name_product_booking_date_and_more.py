# Generated by Django 4.2 on 2023-04-21 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_go', '0011_remove_cart_movie_remove_lineitem_movie_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='booking_date',
            field=models.TextField(default='2000-12-11'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='booking_time',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]