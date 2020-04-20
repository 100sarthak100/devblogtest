from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/index.html',context)

def blogList(request):
    return render(request, 'blog/blogList.html')

def about(request):
    return render(request, 'blog/about.html')

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request, 'blog/blogPost.html',context)