from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from json import load
from validate_email_address import validate_email

# Create your models here.


class User(AbstractUser):
    '''
    This class is for defining the user model whose fields are included username and email, first and last name and gender
    '''
    GENDER = (
        ('mr', 'Man'),
        ('mrs', 'Female')
    )
    username_regex = RegexValidator(
        regex=r'^[a-zA-Z][a-zA-Z0-9]{5,30}$',
        message='Only English letters and numbers are allowed, and the numbers must be after the letters, and the allowed characters are between 6 and 30',
    )
    email_regex = RegexValidator(
        regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        message='Your email is not valid'
    )
    name_regex = RegexValidator(
        regex=r'^[a-zA-Z]{2,30}$',
        message='Only English letters and numbers are allowed, and the allowed characters are between 2 and 30',
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
    first_name = models.CharField(
        max_length=30,
        verbose_name='First Name',
        validators=[name_regex]
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name='Last Name',
        validators=[name_regex]
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER,
        verbose_name='Gender (mr/mrs)'
    )  # choice gender

    USERNAME_FIELD = 'username'  # & Password is required by default.
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'gender']

    def clean(self):
        username = self.username.lower()  # get username
        email = self.email  # get email

        with open('account/username-reserved/username.json', 'r') as usernames:
            username_reserved = load(usernames)

        for item in username_reserved:
            if username == item:  # Checking the username that is not in the reserved usernames
                raise ValidationError('Sorry, this username is not allowed')

        verify_email = validate_email(email, check_mx=True, verify=True)
        if verify_email == None or verify_email == False:  # check valid email
            raise ValidationError(
                'Your email is not valid. Please use a valid email'
            )

    def __str__(self):
        return self.username
