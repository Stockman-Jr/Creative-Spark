from django.shortcuts import render, redirect
from django.views import generic
from .models import Challenge, Post
from . import forms
from django.contrib.auth.decorators import login_required


class ChallengeList(generic.ListView):
    model = Challenge
    template_name = 'index.html'
    queryset = Challenge.objects.all()
    ordering = ["-date_created"]
    paginate_by = 6


class ChallengePostList(generic.ListView):
    model = Post
    ordering = ['-date_posted']
    paginate_by = 6

    def get(self, request, slug, *args, **kwargs):
        challenge = Challenge.objects.get(slug=slug)
        posts = Post.objects.all()
        return render(request, 'challenge_posts.html', context={'posts': posts})
       

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

