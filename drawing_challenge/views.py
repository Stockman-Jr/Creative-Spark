import json
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.models import User
from .models import Challenge, Post, Comment, Like
from users.models import Profile
from .forms import CommentForm, PostForm
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages


class ChallengeList(ListView):
    """
    Home page view, displays a list of all challenges
    """
    model = Challenge
    template_name = 'index.html'
    queryset = Challenge.objects.all()
    ordering = ["-date_created"]
    paginate_by = 6


class PostList(ListView, ModelFormMixin):
    """
    View for all upploaded posts in corresponding challenges,
    also renders the comment form
    """
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

        approved_posts = Post.objects.filter(approved=True)

        if self.request.user.is_authenticated:
            liked = [i for i in Post.objects.all() if Like.objects.filter(user=self.request.user, post=i)]
            faved = [i for i in Post.objects.all() if Profile.objects.filter(user=self.request.user, favourite=i)]

            context['form'] = self.form
            context['post_liked'] = liked
            context['faved'] = faved
        context['approved_posts'] = approved_posts
        return context

    def get_queryset(self):
        return Post.objects.filter(challenge__challenge_prompt=self.kwargs['challenge'])


@login_required
def post(request):
    """
    View to handle user post submissions
    """
    post_form = PostForm()

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)

    if post_form.is_valid():
        form = post_form.save(commit=False)
        form.author = request.user
        messages.add_message(request, messages.SUCCESS, 'Submit sucessful, awaiting approval!')
        form.save()
        return redirect('home')

    challenge = Challenge.objects.all()[0]
    post_form = PostForm(initial={'challenge': challenge})
    return render(request, 'post_upload.html', context={'post_form': post_form})


@login_required
def delete_post(request, pk):
    """
    Handles deletion of user uploaded posts
    """
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        Post.objects.filter(pk=pk).delete()
        messages.success(request, 'Post successfully deleted!')

    return redirect(reverse('my_profile'))


def post_detail(request):
    """
    View to handle comments through ajax
    """
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
    """
    View to handle likes through ajax
    """
    post_id = request.GET.get("likeId", "")
    user = request.user
    post = Post.objects.get(pk=post_id)
    liked = False
    like = Like.objects.filter(user=user, post=post)
    if like:
        liked = False
        like.delete()
    else:
        liked = True
        Like.objects.create(user=user, post=post)
    res = {
        'liked': liked
        }
    response = json.dumps(res)
    return HttpResponse(response, content_type='application/json')


@login_required
def add_favourite(request, pk):
    """
    View that handles adding and removing posts to favourites
    """
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    profile = Profile.objects.get(user=user)

    if profile.favourite.filter(id=pk).exists():
        profile.favourite.remove(post)
    else:
        profile.favourite.add(post)
        messages.add_message(request, messages.SUCCESS, 'Added to favourites!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
