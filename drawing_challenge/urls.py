from . import views
from django.urls import path

urlpatterns = [
    path('challenge/posts/', views.ChallengePostList.as_view(), name='challenge_post'),
    path('', views.ChallengeList.as_view(), name='home'),
    path('post/new/', views.post, name='create_post'),
]