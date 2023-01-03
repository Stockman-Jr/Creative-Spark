from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import ModelFormMixin
from .models import Challenge, Post, Comment
from . import forms
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

