from django import forms
from .models import Post, Comment, Challenge


class PostForm(forms.ModelForm):
    challenge = forms.ModelChoiceField(queryset=Challenge.objects.filter(status='Active'))

    class Meta:
        model = Post
        fields = ['challenge', 'title', 'caption', 'image_post']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
