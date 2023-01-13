from django.contrib import admin
from .models import Challenge, Post, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'post', 'date_created')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'caption', 'image_post', 'challenge', 'approved')
    list_filter = [
        ('approved', admin.BooleanFieldListFilter),
    ]
    actions = ['approve_submission']

    def approve_submission(self, request, queryset):
        queryset.update(approved=True)


class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    readonly_fields = ['author', 'title', 'caption', 'image_post']


class ChallengePostsAdmin(admin.ModelAdmin):
    inlines = [PostInline,]
    list_display = ('challenge_prompt', 'featured_image', 'date_created', 'get_is_active')

    def get_is_active(self, obj):
        return obj.is_active
    get_is_active.boolean = True


admin.site.register(Challenge, ChallengePostsAdmin)
