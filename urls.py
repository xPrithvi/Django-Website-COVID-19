from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name = 'posts_list'),
    path('create/', views.posts_create, name = 'posts_create'),
    path('<id>/', views.posts_detail, name = 'posts_detail'),
    path('update/', views.posts_update, name = 'posts_update'),
    path('delete/', views.posts_delete, name = 'posts_delete'),
]
