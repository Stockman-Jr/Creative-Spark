import io

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Challenge, Post, Comment
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


class TestViews(TestCase):
    """ Tests for views """
    def setUp(self):
        test_user = User.objects.create_user(
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
            author=test_user,
            date_posted=timezone.now(),
            approved=True
        )
        self.comment = Comment.objects.create(content='Test Comment', post=self.post)

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_post_list_page(self):
        response = self.client.get('/posts/' + str(self.challenge.challenge_prompt) + '/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')

    def test_get_past_challenges_page(self):
        response = self.client.get('/challenges/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'past_challenges.html')
    # Site functionality

    def test_add_comment(self):
 
        self.client.post('/comment', {'body': 'Test Comment'})
        self.assertEqual(Comment.objects.last().content, 'Test Comment')