from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from validate_email_address import validate_email

# Create your models here.


class UserManager(BaseUserManager):
    '''
    This class is for user management model
    '''
    def create(self, username, email, firstname, lastname, gender, password=None):

        def verify_email_address(email):
            return validate_email(
                email, 
                check_mx=True, 
                verify=True
            )

        if not username:
            raise ValueError('Users must have a username')
        if verify_email_address(email) == None or verify_email_address == False:
            raise ValidationError('The desired email is invalid. Please enter a valid email')

        user = self.model(
            username=username,
            email=email,
            firstname=firstname,
            lastname=lastname,
            gender=gender,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, firstname, lastname, gender, password):
        user = self.create(
            username=username,
            email=email,
            firstname=firstname,
            lastname=lastname,
            gender=gender,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    '''
    This class is for defining the user model whose fields are included username and email, first and last name and gender
    '''
    GENDER = (
        ('Mr', 'Man'),
        ('mrs', 'Female')
    )
    username_regex = RegexValidator(
        regex=r'^[a-zA-Z][a-zA-Z0-9]{6,30}$',
        message='Only English letters and numbers are allowed and the numbers must be after the letters',
    )
    email_regex = RegexValidator(
        regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        message='Your email is not valid'
    )
    name_regex = RegexValidator(
        regex=r'^[a-zA-Z]{2,30}$',
        message='The format is not valid\nOnly English letters and numbers are allowed',
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
    last_login = models.DateTimeField(auto_now=True, editable=False, blank=True)  # last login user
    account_creation_date = models.DateTimeField(auto_now_add=True, editable=False, blank=True)  # user account creation date

    objects = UserManager()

    USERNAME_FIELD = 'username'  # & Password is required by default.
    REQUIRED_FIELDS = ['email', 'firstname', 'lastname', 'gender']

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    def __str__(self):
        return self.username
