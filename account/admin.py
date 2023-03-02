from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    '''
    This class is the admin panel of the user
    '''
    fieldsets = (
        (None, {"fields": ("username", "password",)}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (("Important dates"), {"fields": ()}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "first_name", "last_name", "password1", "password2",),
            },
        ),
    )
    list_display = ("username", "email", "first_name", "last_name", "gender", "is_staff", "last_login")
    list_filter = ("is_staff", "is_superuser", "is_active", "last_login")
    search_fields = ("username", "first_name", "last_name", "email")
    filter_horizontal = ()
