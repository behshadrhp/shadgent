from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from account import models


@receiver(post_save, sender=models.User)
def create_default_profile(sender, created, instance, **kwargs):
    if created:
        models.Profile.objects.create(owner=instance)
