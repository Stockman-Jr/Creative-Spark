from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from cloudinary.models import CloudinaryField
from django.urls import reverse
from datetime import date, timedelta


STATUS = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
        ]


class Challenge(models.Model):
    """ Drawing Challenges Model """
    title = models.CharField(max_length=200)
    challenge_prompt = models.CharField(max_length=500, unique=True)
    featured_image = CloudinaryField('image')
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS, default='Active')

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.challenge_prompt

    @property
    def is_active(self):
        if (self.date_created.date() + timedelta(days=1)) > date.today():
            self.status = 'Active'
        else:
            self.status = 'Inactive'
            self.save()
        return self.status

    def get_absolute_url(self):
        return reverse("post_list")


class Post(models.Model):
    """User Post Model"""
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='challenges')
    title = models.CharField(max_length=200)
    caption = models.CharField(max_length=1000, blank=True)
    image_post = models.ImageField(upload_to='post_images')
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()


class Comment(models.Model):
    """Model user created comments"""
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(max_length=800)
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.content


class Like(models.Model):
    """Model for liking posts"""
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
