from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from taggit.models import Tag
# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=550)
    content = models.TextField()
    image = models.ImageField(upload_to='blog-images/')
    date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
    
    

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    active = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"commented by {self.user.username}"


class ContactInfo(models.Model):
    map = models.CharField(max_length=250,blank=True,null=True)
    address = models.TextField()
    tel = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    facebook = models.CharField(max_length=250)
    twitter = models.CharField(max_length=250)
    instagram = models.CharField(max_length=250)
    youtube = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Contact Info'
    


class ContactUs(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=500)
    message = models.TextField()
    class Meta:
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return self.subject

