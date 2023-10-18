from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

@receiver(post_save, sender=Profile)
def ensure_profile_exists(sender, instace, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instace)
        print('User and linked profile created successfully')
