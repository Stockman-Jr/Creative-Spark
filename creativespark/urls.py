"""creativespark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('drawing_challenge.urls')),
    path('accounts/', include('allauth.urls')),
    path('users/<slug>/', user_views.profile_view, name='user_profile'),
    path('users/<slug>/favourites', user_views.favourite_list, name='favourite_list'),
    path('my-profile/', user_views.my_profile, name='my_profile'),
    path('my-profile/favourites', user_views.my_favourites, name='my_favourites'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
