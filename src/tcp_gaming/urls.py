"""
URL configuration for tcp_gaming project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from .views import index, concours_view, photo_view, tournoi_view, autres_view

urlpatterns = [
    path('', index, name='index'),
    path('blog/', include("blog.urls")),
    path('admin/', admin.site.urls),
    path('concours/', concours_view, name='concours'),
    path('photo/', photo_view, name='photo'),
    path('tournoi/', tournoi_view, name='tournoi'),
    path('autres/', autres_view, name='autres'),
    path('login/', include("login.urls")),
]
