from django.db import models
from tinymce import HTMLField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    #content = models.TextField()
    content = HTMLField('content')
    author = models.CharField(max_length=20)
    slug = models.CharField(max_length=200)
    tags = TaggableManager()
    timestamp = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return self.title + ' by ' + self.author

    def save(self):
        super().save()
    
        img = Image.open(self.image.path)
    
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='uploads/default.jpg',upload_to='uploads/')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
    
        img = Image.open(self.image.path)
    
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
