from django.shortcuts import render, HttpResponse
from blog.models import Post
from blog.models import Contact
from django.contrib import messages

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/index.html',context)

def blogList(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogList.html', context)

def about(request):
    return render(request, 'blog/about.html')

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request, 'blog/blogPost.html',context)

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent,allPostsAuthor)
    if allPosts.count() == 0:
        messages.warning(request, "No search results found")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'blog/search.html', params)

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been sent")
    return render(request, 'blog/contact.html')