from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    '''
    This class is the admin panel of the user
    '''
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "first_name", "last_name", "password1", "password2",),
            },
        ),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "last_login", "date_joined")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups", "last_login")
