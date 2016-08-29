from django.contrib import admin
from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    # form = SignUpForm
    #class Meta:x
    #    model = SignUp

# admin.site.register(SignUp, SignUpAdmin)

# Define an inline admin descriptor for General model
# which acts a bit like a singleton
# class UserProfileInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False
#     verbose_name_plural = 'User Profile'
#

#@admin.register(Meal)
class MealInline(admin.TabularInline):
    model = Meal
    fields = (
        'name',
        'description',
        'image',
        'price',
        'meetup_time',
        'meetup_location',
        'vegetarian',
        'vegan',
        'gluten_free',
        'lactose_free',
        'nut_free'
    )

class UserAdmin(BaseUserAdmin):
    # fields = (
    #     'username',
    #     'first_name',
    #     'last_name',
    #     'profile_image',
    #     'phone_number'
    # )
    inlines = [MealInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
