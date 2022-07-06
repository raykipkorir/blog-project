from .models import BlogPost, Profile
from users.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    instance.profile.save()
# @receiver(pre_save, sender = BlogPost)
# def blog_owner(sender, instance, **args, **kwargs):
#     instance.user = request.user
    