from django.shortcuts import render
from django.views import generic
from .models import Challenge, Post, PostImage


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

    

