# Generated by Django 4.2 on 2023-04-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_go', '0006_alter_movies_release_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField()),
                ('screenwidth', models.IntegerField()),
                ('aspect_ratio', models.TextField()),
                ('resolution', models.TextField()),
                ('image', models.TextField()),
                ('address', models.TextField()),
                ('cost', models.FloatField()),
            ],
        ),
    ]
