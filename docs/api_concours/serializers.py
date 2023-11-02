from rest_framework import serializers
from .models import Concours, Participant

class ConcoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concours
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'