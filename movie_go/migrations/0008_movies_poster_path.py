# Generated by Django 4.2 on 2023-04-18 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_go', '0007_zones'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='poster_path',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]
