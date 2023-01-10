from django.db import models
from django.db import models
from drawing_challenge.models import Post
from django.contrib.auth.models import User
from PIL import Image
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField
from django.db.models.signals import post_save
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_avatars')
    slug = AutoSlugField(populate_from='user')
    favourite = models.ManyToManyField(Post, blank=True)

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return "/users/{}/".format(self.slug)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass


post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)

