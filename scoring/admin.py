from django.contrib import admin

from scoring.models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'userrole']

@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Application)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'category', 'status', 'application_date']