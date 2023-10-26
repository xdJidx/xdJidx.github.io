from rest_framework import generics
from .models import Tournoi, Participant
from .serializers import TournoiSerializer, ParticipantSerializer

class TournoiListCreate(generics.ListCreateAPIView):
    queryset = Tournoi.objects.all()
    serializer_class = TournoiSerializer

class ParticipantListCreate(generics.ListCreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
