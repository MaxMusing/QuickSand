from .forms import *
from copy import deepcopy
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import *
from django.forms.models import model_to_dict
from django.utils.crypto import get_random_string
from datetime import datetime, time, date
from django.utils import timezone
import re

def landing_page(request):
	if request.user.is_authenticated():
		return redirect('/home/')

	login_form = LogInForm(request.POST or None)
	signup_form = SignUpForm(request.POST or None)
	context = {
		"login_form": login_form,
		"signup_form": signup_form
	}

	return render(request, "landing_page.html", context)

def home(request):
	user = request.user

	if not user.is_authenticated():
		return redirect('/')

	def filter_for_diet(diet_meal_set):
		user = request.user
		veg_bool = getattr(user.userprofile, "vegetarian")
		vegan_bool = getattr(user.userprofile, "vegan")
		gluten_bool = getattr(user.userprofile, "gluten_free")
		lactose_bool = getattr(user.userprofile, "lactose_free")
		nut_bool = getattr(user.userprofile, "nut_free")

		if vegan_bool:
			diet_meal_set = diet_meal_set.filter(vegan=True)
		if veg_bool:
			diet_meal_set = diet_meal_set.filter(vegetarian=True)
		if gluten_bool:
			diet_meal_set = diet_meal_set.filter(gluten_free=True)
		if lactose_bool:
			diet_meal_set = diet_meal_set.filter(lactose_free=True)
		if nut_bool:
			diet_meal_set = diet_meal_set.filter(nut_free=True)

		return diet_meal_set

	now = timezone.now()

	#BUY TAB
	meal_buy_list = []
	non_diet_set = Meal.objects.all().exclude(seller=user)
	diet_set = filter_for_diet(non_diet_set)

	for meal in diet_set:
		isPurchased = getattr(meal, "purchased")
		if not meal.purchased and not meal.expired:
			expire_time = getattr(meal, "meetup_time")
			if expire_time > now:
				meal_buy_list.append(meal)
			else:
				setattr(meal, "expired", True)
				meal.save()

	#SELL TAB
	meal_sell_list = []
	meal_past_sell_list = []
	for user_meal in Meal.objects.filter(seller=user):
		if user_meal.expired:
			meal_past_sell_list.append(user_meal)
		else:
			expire_time = getattr(user_meal, "meetup_time")
			if expire_time > now:
				meal_sell_list.append(user_meal)
			else:
				setattr(user_meal, "expired", True)
				meal_past_sell_list.append(user_meal)
				user_meal.save()

	#PROFILE TAB
	current_purchases = getattr(user.userprofile, "current_purchases")
	try:
		instanceUserProfile = user.userprofile
	except UserProfile.DoesNotExist:
		instanceUserProfile = UserProfile.objects.createUserProfile(user)

	profile_form = ProfileForm(request.POST or None, initial=model_to_dict(instanceUserProfile))
	if profile_form.is_valid():
		first_name = profile_form.cleaned_data.get("first_name")
		last_name = profile_form.cleaned_data.get("last_name")
		profile_image = profile_form.cleaned_data.get("profile_image")
		phone_number = profile_form.cleaned_data.get("phone_number")
		vegan = profile_form.cleaned_data.get("vegan")
		vegetarian = profile_form.cleaned_data.get("vegetarian")
		gluten_free = profile_form.cleaned_data.get("gluten_free")
		lactose_free = profile_form.cleaned_data.get("lactose_free")
		nut_free = profile_form.cleaned_data.get("nut_free")

		userProfile = UserProfile(
			user = user,
			first_name = firstName,
			last_name = last_name,
			phone_number = phone_number,
			profile_image = profile_image,
			vegetarian = vegetarian,
			vegan = vegan,
			gluten_free = gluten_free,
			lactose_free = lactose_free,
			nut_free = nut_free,
			)
		userProfile.save()

	context = {
		"meal_buy_list": meal_buy_list,
		"meal_sell_list": meal_sell_list,
		"profile_form": profile_form,
		"current_purchases": current_purchases,
	}
	return render(request, "home.html", context)

def add_meal(request):
	meal_form = MealForm(request.POST or None)

	context = {
		"meal_form": meal_form
	}

	return render(request, "add_meal.html", context)

def add_meal_request(request):
	meal_form = MealForm(request.POST or None)

	if meal_form.is_valid():
		seller = meal_form.cleaned_data.get("seller")
		name = meal_form.cleaned_data.get("name")
		description = meal_form.cleaned_data.get("description")
		image = meal_form.cleaned_data.get("image")
		price = meal_form.cleaned_data.get("price")
		# meetup_time = meal_form.cleaned_data.get("meetup_time")
		meetup_time = now = timezone.now();
		meetup_location = meal_form.cleaned_data.get("meetup_location")

		vegan = meal_form.cleaned_data.get("vegan")
		vegetarian = meal_form.cleaned_data.get("vegetarian")
		gluten_free = meal_form.cleaned_data.get("gluten_free")
		lactose_free = meal_form.cleaned_data.get("lactose_free")
		nut_free = meal_form.cleaned_data.get("nut_free")

		newMeal = Meal(
			seller = request.user,
			name = name,
			description = description,
			image = image,
			price = price,
			meetup_time = meetup_time,
			meetup_location = meetup_location,

			vegetarian = vegetarian,
			vegan = vegan,
			gluten_free = gluten_free,
			lactose_free = lactose_free,
			nut_free = nut_free,
		)

		newMeal.save();

	return redirect('/home/')

def user_profile_request(request):
	try:
		instanceUserProfile = request.user.userprofile
	except UserProfile.DoesNotExist:
		instanceUserProfile = UserProfile.objects.createUserProfile(request.user)

	profile_form = ProfileForm(request.POST or None, initial=model_to_dict(instanceUserProfile))

	if profile_form.is_valid():
		firstName = profile_form.cleaned_data.get("first_name")
		last_name = profile_form.cleaned_data.get("last_name")
		vegan = profile_form.cleaned_data.get("vegan")
		vegetarian = profile_form.cleaned_data.get("vegetarian")
		gluten_free = profile_form.cleaned_data.get("gluten_free")
		lactose_free = profile_form.cleaned_data.get("lactose_free")
		nut_free = profile_form.cleaned_data.get("nut_free")

		userProfile = UserProfile(
			user = request.user,
			first_name = firstName,
			last_name = last_name,
			vegetarian = vegetarian,
			vegan = vegan,
			gluten_free = gluten_free,
			lactose_free = lactose_free,
			nut_free = nut_free,
			)

		userProfile.save()

	return redirect('/home/')

def login_request(request):
	login_form = LogInForm(request.POST)

	if login_form.is_valid():
		username = login_form.cleaned_data.get("username")
		password = login_form.cleaned_data.get("password")

		if '_login' in request.POST:
	 		user = authenticate(username=username, password=password)
		elif '_signup' in request.POST:
	 		user = User.objects.create_user(username, username, password)
	 		user.save()
	 		userProfile = UserProfile.objects.createUserProfile(user)
	 		user = authenticate(username=username, password=password)
	 		login(request, user)

	if user is not None:
		if user.is_active:
			login(request, user)

	return redirect('/')

def logout_request(request):
	logout(request)
	return redirect('/')

def page_meal(request, meal_id):
	if not request.user.is_authenticated():
		return redirect('/')

	meal = Meal.objects.get(id=meal_id)

	context = {
		"meal": meal,
	}
	return render(request, "page_meal.html", context)

def page_meal_request(request, meal_id):
	user = request.user
	id_user = getattr(user, "id")
	meal = Meal.objects.get(id=meal_id)
	user.userprofile.current_purchases.append(meal)
	setattr(meal, "buyer", getattr(user.userprofile, "first_name"))
	setattr(meal, "purchased", True)
	meal.save()

	return redirect('/')
