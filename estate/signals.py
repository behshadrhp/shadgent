from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from estate import models


@receiver(post_save, sender=models.Estate)
def create_default_sale_or_rent_for_estate(sender, created, instance, **kwargs):
    if created:
        print(instance.type_of_estate_request)
        if instance.type_of_estate_request == 'Sale':
            models.Sale.objects.create(owner=instance.owner, estate=instance)
        elif instance.type_of_estate_request == 'Rent':
            models.Rent.objects.create(owner=instance.owner, estate=instance)
