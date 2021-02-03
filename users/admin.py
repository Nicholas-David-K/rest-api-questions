from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.translation import gettext as _


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'last_name', 'email', 'age']

    ordering = ['id']
    list_display = ['first_name', 'last_name', 'email']
    fieldsets = (
     (None, {'fields': ('email', 'password')}),
     (_('personal Info'), {'fields': ('first_name', 'last_name', 'gender', 'age')}),
     (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
     (_('Inportant dates'), {'fields': ('last_login',)})
   )
    add_fieldsets = (
     (None, {'classes': ('wide',), 'fields': ('first_name', 'last_name', 'email', 'password1', 'password2')}),
   )

admin.site.register(CustomUser, CustomUserAdmin)