from rest_framework import generics
from .models import Concours, Participant
from .serializers import ConcoursSerializer, ParticipantSerializer
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

@method_decorator(staff_member_required, name='dispatch')

class ConcoursListCreate(generics.ListCreateAPIView):
    queryset = Concours.objects.all()
    serializer_class = ConcoursSerializer

@method_decorator(staff_member_required, name='dispatch')

class ParticipantListCreate(generics.ListCreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
