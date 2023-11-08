from django.shortcuts import render, redirect

# Create your views here.

from .models import BlogPost, Tag
from .forms import BlogPostForm, TagForm


def index(request):
    """The home page for the blog."""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}

    # print(context['posts'])

    return render(request, 'blogs/index.html', context)


def new_post(request):
    """Page for adding new blog posts"""

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = BlogPostForm()
    else:
        # POST data submitted, proccess data.
        form = BlogPostForm(data=request.POST)

        # print(request.POST.get('tag'))
        # print(form['tag'].value())
        # return redirect('blogs:index')

        # bak
        if form.is_valid():
            form.save()
            print("Saved new post!")
            return redirect('blogs:index')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


def edit_post(request, post_id):
    """Page to edit existing blog posts"""
    post = BlogPost.objects.get(id=post_id)
    tag = post.tag

    if request.method != 'POST':
        # Initial request. Pre-fill form with the current entry
        form = BlogPostForm(instance=post)
    else:
        # POST data submitted, proccess data.
        form = BlogPostForm(instance=post, data=request.POST)

        if form.is_valid():
            form.save()
            print("Saved modified blog post!")
            return redirect('blogs:post', post_id=post.id)

    # Display a blank or invalid form
    context = {'post': post, 'tag': tag, 'form': form}
    return render(request, 'blogs/edit_post.html', context)


def new_tag(request):
    """Page for adding new tags"""

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = TagForm()
    else:
        # POST data submitted, proccess data.
        form = TagForm(data=request.POST)

        if form.is_valid():
            form.save()
            print("Saved new tag!")
            return redirect('blogs:new_post')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_tag.html', context)


def tag(request, tag_id):
    """Page for viewing posts tagged with tag"""
    tag = Tag.objects.get(id=tag_id)
    posts = tag.blogpost_set.order_by('-date_added')
    context = {'tag': tag, 'posts': posts}

    return render(request, 'blogs/tag.html', context)


def post(request, post_id):
    """Page for viewing a single post"""
    post = BlogPost.objects.get(id=post_id)
    context = {'post': post}
    # tags = tag.tag_set.order_by('name')
    # context = {'post': post, 'tags': tags}

    return render(request, 'blogs/post.html', context)
