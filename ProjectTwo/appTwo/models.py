from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.

DEFAULT_VALUE = '  ' 
class UsersList(models.Model):
    person_id=models.AutoField(primary_key=True)
    person_firstname=models.CharField(max_length=128,)
    person_lastname=models.CharField(max_length=128)
    person_mail=models.EmailField(max_length=264,blank=False,unique=True)

    REQUIRED_FIELD=['person_firstname','person_mail']
    class Meta:
        db_table='users'
        managed=True
        app_label = 'appTwo'

class HotelLocation(models.Model):
    hotel_locations=models.CharField(max_length=264,primary_key=True)
    class Meta:
        db_table='locations'
        managed=True
        app_label = 'appTwo'

class ItemsList(models.Model):
    #item_menu=models.CharField(max_length=264)
    item_name = models.CharField(max_length=30,primary_key=True)
    item_description = models.CharField(max_length=100)
    item_price = models.FloatField(blank=True,null=True)
    item_images=models.ImageField()
    item_rating=models.FloatField()
    class Meta:
        db_table='items'
        managed=True
        app_label = 'appTwo'

class HotelsList(models.Model):
    owner_id=models.OneToOneField(UsersList,on_delete=CASCADE,db_column='owner_id')
    hotel_name=models.CharField(max_length=120,unique=True,primary_key=True)
    hotel_locations=models.ManyToManyField("HotelLocation",default=DEFAULT_VALUE)
    phoneNumberRegex = RegexValidator(regex = r"^\+?91?\d{8,15}$")
    hotel_phonenumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    hotel_rating=models.FloatField()
    hotel_menu=models.ManyToManyField("ItemsList",default=DEFAULT_VALUE)
    class Meta:
        db_table='hotels'
        managed=True
        app_label = 'appTwo'

class ImageFile(models.Model):
    image = models.FileField()
    image_data = models.BinaryField(null=True)
    class Meta:
        db_table='images'
        managed=True
        app_label = 'appTwo'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# @receiver(post_save, sender=UsersList)
# def create_user_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

