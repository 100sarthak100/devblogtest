from django.contrib import admin
from blog.models import Post,Contact,Profile,Comment
 
# Register your models here.

admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Comment)