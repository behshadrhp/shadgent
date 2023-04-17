from django.core.validators import MinValueValidator, MaxValueValidator
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

    # type of estate request
    SALE = 'Sale'
    RENT = 'Rent'

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

    # The type of customer request for the estate
    TYPE_OF_ESTATE_REQUEST = [
        (SALE, 'Sale'),
        (RENT, 'Rent'),
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
    type_of_estate_request = models.CharField(
        max_length=5, choices=TYPE_OF_ESTATE_REQUEST, default=RENT
    )
    meterage = models.PositiveIntegerField()
    number_room = models.PositiveIntegerField()
    number_of_floors = models.PositiveIntegerField(
        default=1, 
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(20)
        ]
    )
    year_made = models.DateField()
    address = models.CharField(max_length=50)

    # property checklist
    elevator = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    yard = models.BooleanField(default=False)