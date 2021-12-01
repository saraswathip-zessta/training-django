# Generated by Django 3.1.13 on 2021-11-12 06:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelLocation',
            fields=[
                ('hotel_locations', models.CharField(max_length=264, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'locations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('image_data', models.BinaryField(null=True)),
            ],
            options={
                'db_table': 'images',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ItemsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30)),
                ('item_description', models.CharField(max_length=100)),
                ('item_price', models.FloatField(blank=True, null=True)),
                ('item_images', models.ImageField(upload_to='')),
                ('item_rating', models.FloatField()),
            ],
            options={
                'db_table': 'items',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UsersList',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('person_firstname', models.CharField(max_length=128)),
                ('person_lastname', models.CharField(max_length=128)),
                ('person_mail', models.EmailField(max_length=264)),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HotelsList',
            fields=[
                ('hotel_name', models.CharField(max_length=120, primary_key=True, serialize=False, unique=True)),
                ('hotel_locations', models.CharField(default='  ', max_length=128)),
                ('hotel_phonenumber', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?91?\\d{8,15}$')])),
                ('hotel_rating', models.FloatField()),
                ('hotel_menu', models.ManyToManyField(default='  ', to='appTwo.ItemsList')),
                ('owner_id', models.OneToOneField(db_column='owner_id', on_delete=django.db.models.deletion.CASCADE, to='appTwo.userslist')),
            ],
            options={
                'db_table': 'hotels',
                'managed': True,
            },
        ),
    ]
