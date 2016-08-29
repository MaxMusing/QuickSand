from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from django import forms
from .models import *



class SignUpForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['username', 'password',]
		labels = {
            "username": "Username",
            "password": "Password",
        }
		widgets = {
	        'password': forms.PasswordInput(),
	    }

	def clean_username(self):
		email = self.cleaned_data['email']
		if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
			raise forms.ValidationError(u'Username "%s" is already in use.' % username)
		return email

	def clean_password(self):
		password = self.cleaned_data.get('password')
		return password

class LogInForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['username', 'password',]
		labels = {
            "username": "Username",
            "password": "Password",
        }
		widgets = {
	        'password': forms.PasswordInput(),
	    }

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		return email

	def clean_password(self):
		password = self.cleaned_data.get('password')
		#validation code
		return password

class ProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = [
			'first_name',
			'last_name',
			'vegetarian',
			'vegan',
			'gluten_free',
			'lactose_free',
			'nut_free'
		]
		labels = {
            "first_name": "First Name",
			"last_name": "Last Name",
			"vegetarian": "Vegetarian",
			"vegan": "Vegan",
			"gluten_free": "Gluten-Free",
			"lactose_free": "Lactose-Free",
			"nut_free": "Nut-Free"
        }

class MealForm(forms.ModelForm):
	class Meta:
		model = Meal
		fields = [
			'name',
			'description',
			'price',
			'image',
			'other_time',
			'meetup_location',
			'vegetarian',
			'vegan',
			'gluten_free',
			'lactose_free',
			'nut_free'
		]
		labels = {
			"name": "Name of Dish",
			"description": "Description",
			"price": "Price",
			"other_time": "Meet-up Time",
			"meetup_location": "Meet-up Location",
			"image": "Image",
			"vegetarian": "Vegetarian",
			"vegan": "Vegan",
			"gluten_free": "Gluten-Free",
			"lactose_free": "Lactose-Free",
			"nut_free": "Nut-Free"
		}
