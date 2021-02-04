from django import forms
from django.contrib.auth.forms import UserChangeForm
from django_registration.forms import RegistrationForm
from .models import CustomUser

class CustomUserCreationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser
    



class CustomUserChangeForm(UserChangeForm):
     class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'gender']



