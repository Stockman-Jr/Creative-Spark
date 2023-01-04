import json
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.models import User
from .models import Challenge, Post, Comment
from .forms import CommentForm, PostForm
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


class ChallengeList(ListView):
    model = Challenge
    template_name = 'index.html'
    queryset = Challenge.objects.all()
    ordering = ["-date_created"]
    paginate_by = 6


class PostList(ListView, ModelFormMixin):
    model = Post
    template_name = 'post_list.html'
    form_class = CommentForm
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        return ListView.get(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):   
        context = super(PostList, self).get_context_data(*args, **kwargs)

        context['form'] = self.form
        return context
     
    def get_queryset(self):
        return Post.objects.filter(challenge__challenge_prompt=self.kwargs['challenge'])


@login_required
def post(request):
    post_form = PostForm()

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)

    if post_form.is_valid():
        form = post_form.save(commit=False)
        form.author = request.user
        form.save()
        return redirect('home')
    return render(request, 'post_upload.html', context={'post_form': post_form})


def post_detail(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    postid = (request.POST.get('post_id'))
    post = get_object_or_404(Post, pk=postid)
    form = CommentForm()
    if request.method == 'POST':
        content = request.POST.get('content')
        form = CommentForm(data=request.POST)

        if form.is_valid():
            comment = Comment()
            comment.name = request.user.username
            comment.content = content
            comment.post = post
            comment.save()
            return JsonResponse(model_to_dict(comment), status=200)

    if is_ajax:
        html = render_to_string('post_detail.html', {'form': form}, request=request)
        return JsonResponse({'form': html})


def like(request):

    if request.POST.get('action') == 'post':
        is_liked = None
        postpk = (request.POST.get('post_pk'))
        post = get_object_or_404(Post, pk=postpk)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            post.save()
            is_liked = False
        else:
            post.likes.add(request.user)
            post.save()
            is_liked = True
        return JsonResponse({'number_of_likes': post.number_of_likes, 'is_liked': is_liked})
    return HttpResponse("Error access denied")
