from django.contrib import admin
from .models import Challenge, Post, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'post', 'date_created')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption', 'image_post', 'challenge', 'approved')
    list_filter = [
        ('approved', admin.BooleanFieldListFilter),
    ]
    actions = ['approve_submission']

    def approve_submission(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Challenge)

