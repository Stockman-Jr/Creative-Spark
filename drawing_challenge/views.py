from django.shortcuts import render, redirect
from django.views import generic
from .models import Challenge, Post, PostImage
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
    template_name = "challenge_posts.html"

#    def get(self, request, slug, *args, **kwargs):
#        challenge = Challenge.objects.get(slug=slug)
#        queryset = Post.objects.order_by('-date_posted')

@login_required
def post(request):
    post_form = forms.PostForm()
    image_form = forms.ImageForm()

    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        image_form = forms.ImageForm(request.POST, request.FILES)

    if post_form.is_valid() and image_form.is_valid():
        form = post_form.save(commit=False)
        form.author = request.user
        photo = image_form.save()
        return redirect('home')
    return render(request, 'post_upload.html', context={'post_form': post_form, 'image_form': image_form})

