from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


class UserAdminModel(admin.ModelAdmin):
    list_filter = ['email', 'first_name', 'last_name']
    list_display = ['first_name', 'last_name', 'email', 'is_admin']


admin.site.register(User, UserAdminModel)
