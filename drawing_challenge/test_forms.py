from django.test import TestCase
from .forms import PostForm, CommentForm


class TestCommentForm(TestCase):
    def test_content_field_is_required(self):
        form = CommentForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')


class TestPostForm(TestCase):
    def test_title_field_is_required(self):
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_image_post_field_is_required(self):
        form = PostForm({'image_post': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('image_post', form.errors.keys())
        self.assertEqual(form.errors['image_post'][0], 'This field is required.')

    def test_challenge_field_is_required(self):
        form = PostForm({'challenge': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('challenge', form.errors.keys())
        self.assertEqual(form.errors['challenge'][0], 'This field is required.')