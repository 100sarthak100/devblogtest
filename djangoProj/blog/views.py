from django.shortcuts import render, HttpResponse,get_object_or_404,redirect
from blog.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.models import Contact
from django.contrib import messages
from taggit.models import Tag
from .forms import (
    UserRegisterForm,
    UserUpdateForm, 
    ProfileUpdateForm)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from datetime import datetime


# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/index.html',context)

# function based approach (old)
# def blogList(request):
#     allPosts = Post.objects.all()
#     context = {'allPosts': allPosts}
#     return render(request, 'blog/blogList.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/blogList.html'
    context_object_name = 'allPosts'
    ordering = ['-timestamp']
    paginate_by = 5

# function based approach (old)
# def blogPost(request, slug):
#     post = Post.objects.filter(slug=slug).first()
#     context = {'post':post}
#     return render(request, 'blog/blogPost.html',context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blogPost.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content','tags']

    def form_valid(self, form):
        form.instance.author = str(self.request.user)
        form.instance.timestamp = datetime.now()
        form.save()
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content','tags']

    def form_valid(self, form):
        form.instance.author = str(self.request.user)
        #form.instance.timestamp = datetime.now()
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if str(self.request.user) == str(post.author):
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if str(self.request.user) == str(post.author):
            return True
        return False



def about(request):
    return render(request, 'blog/about.html')


def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPostsTags = Post.objects.filter(tags__name=query)
        allPosts = allPostsTitle.union(allPostsContent,allPostsAuthor,allPostsTags)
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


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    allPosts = Post.objects.filter(tags=tag)
    context = {
        'allPosts':allPosts,
        'query':tag,
    }
    return render(request, 'blog/search.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'blog/profile.html', context)

@login_required
def comment_approve(request, pk,):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blogPost', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blogPost', pk=comment.post.pk)

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blogPost', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})