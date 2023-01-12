from . import views
from django.urls import path

urlpatterns = [
    path('', views.ChallengeList.as_view(), name='home'),
    path('posts/<str:challenge>/', views.PostList.as_view(), name='post_list'),
    path('comment/', views.post_detail, name='post_detail'),
    path('like/', views.like, name='post_like'),
    path('favourite/<int:pk>', views.add_favourite, name='add_favourite'),
    path('post/new/', views.post, name='create_post'),
    path('delete/<int:pk>', views.delete_post, name='delete_post'),
]