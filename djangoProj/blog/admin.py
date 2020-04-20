from django.contrib import admin
from blog.models import Post
from blog.models import Contact
from blog.models import Profile
# Register your models here.

admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Profile)