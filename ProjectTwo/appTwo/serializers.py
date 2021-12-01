from rest_framework import serializers
from django.contrib.auth.models import User
from appTwo.models import ItemsList

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=ItemsList
        fields="__all__"
 
class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields =  '__all__'


 
   