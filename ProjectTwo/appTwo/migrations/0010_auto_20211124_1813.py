# Generated by Django 3.1.13 on 2021-11-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0009_hotelslist_hotel_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userslist',
            name='person_mail',
            field=models.EmailField(max_length=264, unique=True),
        ),
    ]
