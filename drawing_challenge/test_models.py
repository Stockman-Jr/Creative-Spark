import io
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Challenge, Post, Comment, Like
from django.core.files import File
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from django.core.files.base import ContentFile


def get_temp_image():
    image_file = io.BytesIO()
    image = Image.new('RGB', size=(50, 50), color=(255, 0, 0))
    image.save(image_file, 'png')
    image_file.seek(0)
    test_image = ContentFile(image_file.read(), 'test.png')
    return test_image


class TestModels(TestCase):
    """ Tests for views """
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='userpw'
        )
        self.client.login(username='testuser', password='userpw')
        self.challenge = Challenge.objects.create(
            title='Draw Test',
            challenge_prompt='Test Challenge',
            featured_image=File(file=b""),
            date_created=timezone.now(),
            status='Active')
        self.post = Post.objects.create(
            challenge=self.challenge,
            title='Test',
            caption='Test Caption',
            image_post=get_temp_image(),
            author=self.user,
            date_posted=timezone.now(),
            approved=True
        )
        self.comment = Comment.objects.create(
            post=self.post,
            content='Test Comment', 
            name='testuser'
            )
        self.like = Like.objects.create(user=self.user, post=self.post)

    def test_challenge_string_method_returns_challenge_prompt(self):
        self.assertEqual(self.challenge.__str__(), 'Test Challenge')
 

    def test_post_string_method_returns_title(self):
        self.assertEqual(self.post.__str__(), 'Test')

    def test_comment_string_method_returns_content(self):
        self.assertEqual(self.comment.__str__(), 'Test Comment')