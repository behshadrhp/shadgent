from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    GENDER = (
        ('Mr', 'Man'),
        ('mrs', 'Female')
    )
    username_regex = RegexValidator(
        regex=r'^[a-zA-Z][a-zA-Z0-9]{6,30}$',
        message='Only English letters and numbers are allowed',
    )
    email_regex = RegexValidator(
        regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        message='Your email is not valid'
    )
    name_regex = RegexValidator(
        regex=r'^[a-zA-Z]{2,30}$',
        message='The format is not valid',
    )
    username = models.CharField(
        unique=True,
        max_length=30,
        validators=[username_regex]
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='Email Address',
        validators=[email_regex]
    )
    firstname = models.CharField(
        max_length=30,
        verbose_name='first name',
        validators=[name_regex]
    )
    lastname = models.CharField(
        max_length=30,
        verbose_name='last name',
        validators=[name_regex]
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER,
    )  # choice gender
    is_active = models.BooleanField(default=True)  # active account
    is_staff = models.BooleanField(default=False)  # access to admin panel
    is_admin = models.BooleanField(default=False)  # admin user / not superuser
    is_superuser = models.BooleanField(default=False)  # superuser
    last_login = models.DateTimeField(auto_now=True)  # last login user
    account_creation_date = models.DateTimeField(auto_now_add=True)  # user account creation date

    USERNAME_FIELD = 'username'  # & Password is required by default.
    REQUIRED_FIELDS = ['email', 'lastname', 'firstname', 'gender']

    def __str__(self):
        return self.username
