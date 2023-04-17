from django.contrib import admin
from estate import models


@admin.register(models.Estate)
class EstateAdmin(admin.ModelAdmin):
    '''This class is for the Estate model in the admin panel'''

    list_display = [
        'owner',
        'title',
        'status_estate',
        'type_of_property_estate',
        'type_of_estate_request',
        'meterage',
        'number_room',
        'number_of_floors',
        'year_made',
    ]
    list_filter = [
        'status_estate',
        'type_of_property_estate',
        'type_of_estate_request',
        'number_room',
        'number_of_floors',
    ]
    search_fields = [
        'owner__icontains',
        'title__icontains',
        'description__icontains',
        'status_estate__icontains',
        'type_of_property_estate__icontains',
        'type_of_estate_request__icontains',
    ]
    fields = [
        'title',
        'description',
        'address',
        'year_made',
        'status_estate',
        'type_of_property_estate',
        'type_of_estate_request',
        'meterage',
        'number_room',
        'number_of_floors',
        'elevator',
        'parking',
        'yard',
    ]
    list_per_page = 10

    def owner(self, owner: models.Estate.owner):
        return f'{owner.username}'

    # save estate model
    def save_model(self, request, obj, form, change):
        # change owner field to owner requested
        obj.owner = request.user
        return super().save_model(request, obj, form, change)
