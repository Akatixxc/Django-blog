from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostModelForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile

# Create Retrieve Update Delete

def posts_list(request):
    all_posts = Post.objects.order_by('-date').all()
    context = {
        'all_posts': all_posts
    }
    return render(request, "posts/posts_list.html", context)

def posts_detail(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    context = {
        'post': unique_post
    }
    return render(request, "posts/posts_detail.html", context)

@login_required
def posts_create(request):
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author, created = Profile.objects.user.get_or_cerate(
            user=request.user,
        )
        form.save()
        return redirect('posts-list')
    context = {
        'form': form,
        'title': 'Create'
    }
    return render(request, "posts/posts_create.html", context)

def posts_update(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    form = PostModelForm(request.POST or None, request.FILES or None, instance=unique_post)
    if form.is_valid():
        form.save()
        return redirect('/posts/')
    context = {
        'form': form
    }
    return render(request, "posts/posts_create.html", context)

def posts_delete(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    unique_post.delete()
    return redirect('/posts/')