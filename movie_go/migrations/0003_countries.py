# Generated by Django 4.2 on 2023-04-14 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_go', '0002_languages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_countries', models.TextField()),
            ],
        ),
    ]
