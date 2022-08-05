from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

User = get_user_model()

@receiver(post_save, sender=User)
def user_profile_created(sender, created, instance, *args, **kwargs):
    if created:
        user = instance
        Profile.objects.create(user=user)