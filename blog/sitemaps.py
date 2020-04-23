from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.urls import reverse

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Post.objects.all()

class StaticViewSitemap(Sitemap):
    priority = 1.0

    def items(self):
        return ['about','contact','blogHome','blogList','profile','login','logout','register']

    def location(self, item):
        return reverse(item)