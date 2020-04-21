from django.contrib import admin
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    #UserPostListView,
)
from . import views


urlpatterns = [
    path('',views.blogHome, name='blogHome'),
    #path('blogList/', views.blogList, name='blogList' ),
    path('blogList/', PostListView.as_view(), name='blogList' ),
    path('about/', views.about, name="about"),
    #path('blog/<str:slug>',views.blogPost, name='blogPost'),
    path('blog/<int:pk>/',PostDetailView.as_view(), name='blogPost'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('blog/new/',PostCreateView.as_view(), name='post-create'),
    path('register/', views.register, name='register'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('blog/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]