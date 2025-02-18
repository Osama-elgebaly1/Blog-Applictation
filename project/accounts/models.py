from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  #
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='accounts-images/')
    bio = models.TextField(max_length=150)

    def __str__(self):
        return self.name


# Using signals to create a profile authomatic 
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile = Profile(user=instance,name=instance.username)
        profile.save()

post_save.connect(create_profile,sender=User)

