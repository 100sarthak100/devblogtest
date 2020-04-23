from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.urls import reverse

class PostSitemap(Sitemap):

    def items(self):
        return Post.objects.all()

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['about','contact','blogHome','blogList','profile','login','logout','register']

    def location(self, item):
        return reverse(item)