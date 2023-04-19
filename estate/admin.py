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


@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):
    '''This class is for the Sale model in the admin panel'''''

    list_display = [
        'owner',
        'estate',
        'price_per_meter',
        'discount',
        'discount_price',
        'final_price',
        'exchange',
    ]
    list_filter = []
    search_fields = []
    fields = [
        'estate',
        'price_per_meter',
        'discount',
        'exchange',
    ]
    list_per_page = 10

    def owner(self, owner: models.Estate.owner):
        return f'{owner.username}'

    # this function is for calculate discount price
    def discount_price(self, sale: models.Sale):
        Initialـprice = sale.price_per_meter * sale.estate.meterage
        discount = sale.discount
        final_price = ((discount / 100) * Initialـprice)
        return final_price

    # this function is for calculate final price
    def final_price(self, sale: models.Sale):
        Initialـprice = sale.price_per_meter * sale.estate.meterage
        discount = sale.discount
        amount = ((discount / 100) * Initialـprice)
        final_price = (Initialـprice - amount)
        return final_price

    # save estate model
    def save_model(self, request, obj, form, change):
        # change owner field to owner requested
        obj.owner = request.user
        return super().save_model(request, obj, form, change)
