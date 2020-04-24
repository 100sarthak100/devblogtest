from django.db import models
from tinymce import HTMLField
from django.utils import timezone
from taggit.managers import TaggableManager
from django.urls import reverse
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
    image = models.ImageField(default='uploads/default.jpg',upload_to ='uploads/')

    def __str__(self):
        return self.title + ' by ' + self.author

    def get_absolute_url(self):
        return reverse('blogPost', kwargs={'pk': self.pk})

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    # def save(self):
    #     super().save()
    
    #     img = Image.open(self.image.path)
    
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    
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
    
    # def save(self, *args, **kawrgs):
    #     super().save(*args, **kawrgs)
    
    #     img = Image.open(self.image.path)
    
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
