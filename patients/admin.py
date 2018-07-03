from django.contrib import admin
from .models import ( Biometric, Lab, Initial, Medication,
Allergy,Diagnose,Meal,Week,Exercise,Plan,Illness,Allergen,Drug,Insurance,Referrer,
Day,Test,Ethnicity,Country,State,Checklist,Checklistitems,Branch,Profile,Programtype)
# Register your models here.
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms

admin.site.register(Initial)
# admin.site.register(Profile)
admin.site.register(Programtype)
# admin.site.register(Info)
admin.site.register(Biometric)
admin.site.register(Lab)

admin.site.register(Medication)
admin.site.register(Allergy)
admin.site.register(Diagnose)
admin.site.register(Meal)
admin.site.register(Week)
admin.site.register(Exercise)
admin.site.register(Plan)
admin.site.register(Illness)
admin.site.register(Allergen)
admin.site.register(Drug)
admin.site.register(Insurance)
admin.site.register(Referrer)
admin.site.register(Day)
admin.site.register(Test)
admin.site.register(Ethnicity)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Checklistitems)
admin.site.register(Checklist)
admin.site.register(Branch)
# admin.site.register(UserProfileInfo)
# @admin.register(Info)
# class InfoAdmin(admin.ModelAdmin):
#     fields = ('name','preferred_name', 'date_of_birth', 'height', 'initial', 'insurance','phone','gender','ethnicity',
#                 'address1','address2','country','state','notes','profile_pic')


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profile'
#
# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileInline,)
#
# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('first_name','insurance','profile_pic')
