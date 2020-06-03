from django.contrib import admin
from blog.models import Post,Contact,Profile,Comment
 
# Register your models here.
#from djangoseo.admin import register_seo_admin
# from django.contrib import admin
# from blog.seo import MyMetadata

# register_seo_admin(admin.site, MyMetadata)

admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Comment)

