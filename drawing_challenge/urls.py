from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>', views.ChallengePostList.as_view(), name='challenge_post'),
    path('', views.ChallengeList.as_view(), name='home'),
]