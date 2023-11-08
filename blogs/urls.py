"""Defines URL patterns for blogs."""

from django.urls import path

from . import views


app_name = 'blogs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for adding a new blog post
    # path('new_post/<int:tag_id>/', views.new_post, name='new_post'),
    path('new_post/', views.new_post, name='new_post'),
    # Page for editing a blog post
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    # Page for adding a new tag
    path('new_tag/', views.new_tag, name='new_tag'),
    # Page to view all posts for a given tag
    path('tag/<int:tag_id>/', views.tag, name='tag'),
    # Page to view a single post
    path('post/<int:post_id>/', views.post, name='post'),
]
