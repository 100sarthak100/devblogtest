from django.db import models
from tinymce import HTMLField

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    #content = models.TextField()
    content = HTMLField('content')
    author = models.CharField(max_length=20)
    slug = models.CharField(max_length=200)
    timestamp = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return self.title + ' by ' + self.author
    
