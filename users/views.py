from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from drawing_challenge.models import Post, Challenge
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def profile_view(request, slug):
    Profile.objects.get_or_create(user=request.user)
    p = Profile.objects.filter(slug=slug).first()
    p_user = p.user
    user_posts = Post.objects.filter(author=p_user).order_by('-date_posted')
    post_count = Post.objects.filter(author=p_user).count()

    context = {
        'p_user': p_user,
        'user_posts': user_posts,
        'post_count': post_count,
        'p': p,
    }

    return render(request, 'users/profile.html', context)


@login_required
def my_profile(request):
    Profile.objects.get_or_create(user=request.user)
    p = request.user.profile
    current_user = p.user
    user_posts = Post.objects.filter(author=current_user).order_by('-date_posted')
    post_count = Post.objects.filter(author=current_user).count()

    context = {
        'p_user': current_user,
        'user_posts': user_posts,
        'post_count': post_count,
    }

    return render(request, 'users/profile.html', context)
