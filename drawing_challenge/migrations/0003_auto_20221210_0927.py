# Generated by Django 3.2.16 on 2022-12-10 09:27

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drawing_challenge', '0002_rename_challenges_challenge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_post', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='drawing_challenge.post')),
            ],
        ),
    ]