from rest_framework import serializers
from .models import Tournoi, Participant

class TournoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournoi
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
