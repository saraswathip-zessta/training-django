from django import forms
from django.forms import ModelForm
from appTwo.models import HotelsList,ImageFile, UsersList
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UploadImageForm(ModelForm): # Form for uploading an image
    class Meta:
        model = ImageFile
        fields = ['image']

class SearchInfoForm(ModelForm): #Form to list the hotel details 
    class Meta:
        model = HotelsList
        fields = "__all__"  

            
class NewUserForm(UserCreationForm): #Form for New user registration 
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class UserForm(ModelForm):#Form for update of user data

	class Meta:
		model = UsersList
		fields = ("person_id","person_firstname","person_lastname","person_mail")

	# def clean(self):
	# 	person_firstname= self.cleaned_data.get('person_firstname')