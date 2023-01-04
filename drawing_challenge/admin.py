from django.contrib import admin
from .models import Challenge, Post, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'post', 'date_created')


admin.site.register(Challenge)
admin.site.register(Post)
