from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile

# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    '''This class is the admin panel of the user'''

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "first_name", "last_name", "password1", "password2",),
            },
        ),
    )
    list_display = ("username", "email", "first_name",
                    "last_name", "is_staff", "last_login", "date_joined")
    list_filter = ("is_staff", "is_superuser",
                   "is_active", "groups", "last_login")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''This class is for admin panel of the profile'''

    list_display = [
        'owner',
        'phone_number',
        'gender',
        'create_at',
    ]
    list_filter = [
        'gender',
    ]
    search_fields = [
        'owner__username__icontains',
        'phone_number__icontains',
        'create_at__icontains'
    ]
    fields = [
        'phone_number',
        'picture',
        'bio',
        'birthday',
        'gender',
    ]
    list_per_page = 10

    # save estate model
    def save_model(self, request, obj, form, change):
        # change owner field to owner requested
        obj.owner = request.user
        return super().save_model(request, obj, form, change)
