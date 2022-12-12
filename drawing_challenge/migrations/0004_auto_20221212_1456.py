# Generated by Django 3.2.16 on 2022-12-12 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drawing_challenge', '0003_auto_20221210_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_post',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
        migrations.AddField(
            model_name='post',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='drawing_challenge.challenge'),
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
