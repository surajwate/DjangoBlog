from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# This is a receiver function that gets the signal and performs some task.
# In this case, our task is to create a profile object whenever a user is created.
# The receiver function takes the signal and the sender as arguments.
# The signal is the post_save signal that was sent by the User model.
# The sender is the User model itself.
# So when a user is saved, send this signal (post_save).
# The receiver is the create_profile function.
# The post_save signal gets fired after an object is saved.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()