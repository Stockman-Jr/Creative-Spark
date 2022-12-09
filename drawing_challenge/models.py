from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Challenge(models.Model):
    title = models.CharField(max_length=200)
    challenge_prompt = models.CharField(max_length=500, unique=True)
    featured_image = CloudinaryField('image')
    slug = models.SlugField(max_length=200, unique=True)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    caption = models.CharField(max_length=1000, blank=True)
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.caption

    def number_of_likes(self):
        return self.likes.count()


# class PostImage(models.Model):
#    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
#    image = CloudinaryField('image', default='placeholder')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=800, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.content

