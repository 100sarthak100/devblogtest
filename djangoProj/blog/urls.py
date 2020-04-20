from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views

urlpatterns = [
    path('',views.blogHome, name='blogHome'),
    #path('blogList/', views.blogList, name='blogList' ),
    path('blogList/', PostListView.as_view(), name='blogList' ),
    path('about/', views.about, name="about"),
    #path('blog/<str:slug>',views.blogPost, name='blogPost'),
    path('blog/<int:pk>/',PostDetailView.as_view(), name='blogPost'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('blog/new/',PostCreateView.as_view(), name='post-create'),
]