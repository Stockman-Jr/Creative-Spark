from . import views
from django.urls import path

urlpatterns = [
    path('', views.ChallengeList.as_view(), name='home')
]