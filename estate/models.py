from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from djmoney.models.fields import MoneyField
from estate.validator import english_regex


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

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=50,
        unique=True,
        validators=[
            RegexValidator(
                english_regex, 'Only numbers and English letters from 5 to 50 characters are allowed'
            )
        ],
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        allow_unicode=True,
        validators=[
            RegexValidator(
                english_regex, 'Only numbers and English letters from 5 to 50 characters are allowed'
            )
        ],
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
    description = models.TextField(null=True, blank=True)
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

    # create - update Time
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # Save the slug with the title input parameter
    def save(self, *args, **kwargs):
        if not self.title or self.title != self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Estate, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-update_at']


class Sale(models.Model):
    '''This class is for pricing based on estate sale parameters'''

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    estate = models.OneToOneField(
        Estate,
        on_delete=models.CASCADE
    )
    price_per_meter = MoneyField(
        max_digits=14, decimal_places=0, default_currency='USD', default=0
    )
    discount = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ]
    )

    # property checklist
    exchange = models.BooleanField(default=False)

    # create - update Time
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.estate.title

    class Meta:
        ordering = ['-update_at']


class Rent(models.Model):
    '''This class is for pricing real estate lease and mortgage'''

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    estate = models.OneToOneField(
        Estate,
        on_delete=models.CASCADE
    )
    annual_mortgage = MoneyField(
        max_digits=14, decimal_places=0, default_currency='USD', default=0
    )
    rent_of_months = MoneyField(
        max_digits=14, decimal_places=0, default_currency='USD', default=0
    )

    # property checklist
    exchange = models.BooleanField(default=False)

    # create - update Time
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.estate.title

    class Meta:
        ordering = ['-update_at']
