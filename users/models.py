from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
# Create your models here.


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, gender, password=None, **extra_fields):

        if not email:
            raise ValueError('Email Address is Required')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name, 
            gender=gender
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, first_name, last_name, email, gender,password=None, **extra_fields):
        user = self.create_user(first_name=first_name, last_name=last_name, email=email, gender=gender, password=password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # username = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


    def get_short_name(self):
        return self.first_name

    
    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        
