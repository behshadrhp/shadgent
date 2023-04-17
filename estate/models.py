from django.conf import settings
from django.db import models

# Create your models here.


class Estate(models.Model):
    '''This class is for receive property estate information'''

    # status estate
    VILLA = 'Villa'
    APARTMENT = 'Apartment'
    SHOP = 'Shop'

    # type of property estate
    COMMERCIAL = 'Commercial'
    OFFICIAL = 'Official'
    RESIDENTIAL = 'Residential'

    # Selection parameters of estate status
    STATUE_ESTATE = [
        (VILLA, 'Villa'),
        (APARTMENT, 'Apartment'),
        (SHOP, 'Shop'),
    ]

    # Selection parameters of type property estate
    TYPE_OF_PROPERTY_ESTATE = [
        (COMMERCIAL, 'Commercial'),
        (OFFICIAL, 'Official'),
        (RESIDENTIAL, 'Residential'),
    ]

    User = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_estate = models.CharField(
        max_length=10, choices=STATUE_ESTATE, default=VILLA
    )
    type_of_property_estate = models.CharField(
        max_length=12, choices=TYPE_OF_PROPERTY_ESTATE, default=COMMERCIAL
    )
    meterage = models.PositiveIntegerField()
    number_room = models.PositiveIntegerField()
    year_made = models.DateField()
    address = models.CharField(max_length=50)
