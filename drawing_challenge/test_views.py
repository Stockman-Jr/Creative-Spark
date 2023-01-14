from django.test import TestCase
from django.contrib.auth.models import User
from .models import Challenge, Post, Comment
from django.core.files import File
from django.utils import timezone


class TestViews(TestCase):
    """ Tests for views """

    def setUp(self):
        test_user = User.objects.create_user(
            username='testuser',
            password='userpw'
        )
        self.client.login(username='testuser', password='userpw')
        self.challenge = Challenge.objects.create(title='Draw Test', challenge_prompt='Test Challenge', featured_image=File(file=b""), date_created=timezone.now(), status='Active')
        self.post = Post.objects.create(
            challenge=self.challenge,
            title='Test',
            caption='Test Caption',
            image_post=File(file=b""),
            author=test_user,
            date_posted=timezone.now(),
            approved=True
        )
        self.comment = Comment.objects.create(content='Test Comment', post=self.post)

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')