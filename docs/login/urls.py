from django.urls import path
from login import views

urlpatterns = [
    path('', views.index, name="login-index"),
    path('register/', views.register, name='register'),
    path('connect/', views.connect, name='connect'),
    path('logout/', views.logout_view, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]