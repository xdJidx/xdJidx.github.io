from django.urls import path
from .views import TournoiListCreate, ParticipantListCreate

urlpatterns = [
    path('tournois/', TournoiListCreate.as_view(), name='tournoi-list-create'),
    path('participants/', ParticipantListCreate.as_view(), name='participant-list-create'),
]
