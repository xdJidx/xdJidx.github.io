from django.urls import path
from .views import CreerConcours

urlpatterns = [
    path('creer_concours/', CreerConcours.as_view(), name='creer_concours'),
    # Autres URL
]