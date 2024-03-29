import io
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Challenge, Post, Comment, Like
from users.models import Profile
from django.core.files import File
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from django.utils.timezone import now
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
        self.user = User.objects.create_user(
            username='testuser',
            password='userpw'
        )
        self.client = Client()
        self.client.login(username='testuser', password='userpw')
        self.challenge = Challenge.objects.create(
            title='Draw Test',
            challenge_prompt='Test Challenge',
            featured_image=File(file=b""),
            date_created=now().date(),
            status='Active')
        self.post = Post.objects.create(
            challenge=self.challenge,
            title='Test',
            caption='Test Caption',
            image_post=get_temp_image(),
            author=self.user,
            date_posted=now().date(),
            approved=True
        )
        self.comment = Comment.objects.create(
            content='Test Comment', post=self.post
            )
        self.like = Like.objects.create(user=self.user, post=self.post)

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        challenge_list = response.context['challenge_list']
        for challenge in challenge_list:
            self.assertTrue(challenge.is_active)

        self.assertTemplateUsed(response, 'index.html')

    def test_get_post_list_page(self):
        response = self.client.get('/posts/' + str(
            self.challenge.challenge_prompt) + '/'
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')

    def test_get_past_challenges_page(self):
        response = self.client.get('/challenges/')
        self.assertEqual(response.status_code, 200)

        challenge_list = response.context['challenge_list']
        self.challenge.status == 'Inactive'
        for challenge in challenge_list:
            self.assertFalse(challenge.is_active)

        self.assertTemplateUsed(response, 'past_challenges.html')

    def test_get_post_upload_page(self):
        response = self.client.get('/post/new/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_upload.html')

    def test_post_upload_page_initial_value(self):
        response = self.client.get('/post/new/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['post_form'].initial['challenge'], self.challenge
            )

    def test_can_add_comment(self):
        self.client.login(username='testuser', password='userpw')

        self.client.post('/comment', {
            'name': self.user, 'body': 'Test Comment'
            })
        self.assertEqual(Comment.objects.last().content, 'Test Comment')
