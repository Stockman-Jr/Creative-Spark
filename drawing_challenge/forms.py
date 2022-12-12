from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'caption', 'image_post']


# class ImageForm(forms.ModelForm):
#    class Meta:
#        model = PostImage
#        fields = ['image_post', ]