from __future__ import unicode_literals
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

#Models
class UserProfileManager(models.Manager):
	def createUserProfile(self, user):
		userProfile = self.create(user=user)
		return userProfile

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	objects = UserProfileManager()
	password = models.CharField(max_length=35, blank=False, null=False)
	username = models.CharField(max_length=25, null=False, blank=False)
	first_name = models.CharField(max_length=50, null=False, blank=False)
	last_name = models.CharField(max_length=50, null=False, blank=False)

	#Dietary Restrictions
	vegetarian = models.BooleanField(default=False)
	vegan = models.BooleanField(default=False)
	gluten_free = models.BooleanField(default=False)
	lactose_free = models.BooleanField(default=False)
	nut_free = models.BooleanField(default=False)

	current_rating = 0
	rating_list = []

	current_purchases = []

	def __unicode__(self):
		return self.first_name + self.last_name + self.phone_number

class Meal(models.Model):

	buyer = ""
	seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	expired = False
	purchased = False

	name = models.CharField(max_length=50, null=False, blank=False)
	description = models.CharField(max_length=5000, null=False, blank=False)
	image = models.ImageField(null=False, blank=False)
	price = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)
	meetup_time = models.DateTimeField(null=True, blank=True)
	other_time = models.CharField(max_length=50, null=True, blank=True)
	meetup_location = models.CharField(max_length=50, null=False, blank=False)

	vegetarian = models.BooleanField(default=False)
	vegan = models.BooleanField(default=False)
	gluten_free = models.BooleanField(default=False)
	lactose_free = models.BooleanField(default=False)
	nut_free = models.BooleanField(default=False)

	def name_url(self):
		return self.name.replace(' ', '-')

	def __unicode__(self):
		return self.name
