from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def create_profile_and_group(sender, instance, created, **kwargs):
    if created:
# Default to student unless specified later
        profile = UserProfile.objects.create(user=instance, role="student")
        group, _ = Group.objects.get_or_create(name="Student")
        instance.groups.add(group)