from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Challenge, Post
from . import forms
from django.contrib.auth.decorators import login_required


class ChallengeList(ListView):
    model = Challenge
    template_name = 'index.html'
    queryset = Challenge.objects.all()
    ordering = ["-date_created"]
    paginate_by = 6


class ChallengePostList(ListView):
    model = Post
    template_name = 'challenge_posts.html'
    queryset = Post.objects.all()
    ordering = ['-date_posted']
    paginate_by = 6


@login_required
def post(request):
    post_form = forms.PostForm()

    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, request.FILES)

    if post_form.is_valid():
        form = post_form.save(commit=False)
        form.author = request.user
        form.save()
        return redirect('home')
    return render(request, 'post_upload.html', context={'post_form': post_form})

