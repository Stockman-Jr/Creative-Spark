from django import forms
from .models import Post, Comment, Challenge


class PostForm(forms.ModelForm):
    challenge = forms.ModelChoiceField(queryset=Challenge.objects.filter(status='Active'))

    class Meta:
        model = Post
        fields = ['title', 'caption', 'image_post', 'challenge']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
