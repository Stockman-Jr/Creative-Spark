from django.contrib import admin
from .models import Challenge, Post, Comment, Like


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'post', 'date_created')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'likes_count', 'challenge', 'approved')
    readonly_fields = ['author', 'title', 'caption', 'image_post']
    list_filter = [
        ('approved', admin.BooleanFieldListFilter),
    ]
    actions = ['approve_submission']

    def likes_count(self, obj):
        return len(obj.likes.all())
    likes_count.short_description = 'Likes'

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).prefetch_related('likes')

    def approve_submission(self, request, queryset):
        queryset.update(approved=True)


class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    readonly_fields = ['author', 'title', 'caption', 'image_post']


class ChallengePostsAdmin(admin.ModelAdmin):
    inlines = [PostInline,]
    list_display = ('challenge_prompt', 'featured_image', 'date_created')
    list_display = ('challenge_prompt', 'title', 'date_created', 'status')


admin.site.register(Challenge, ChallengePostsAdmin)
