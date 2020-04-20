from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogHome, name='blogHome'),
    path('blogList/', views.blogList, name='blogList' ),
    path('about/', views.about, name="about"),
    path('blog/<str:slug>',views.blogPost, name='blogPost'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
]