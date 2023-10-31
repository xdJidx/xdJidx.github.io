from django.http import HttpResponse
from django.template import loader
from django.views.decorators.clickjacking import xframe_options_exempt
import os
from django.conf import settings
from rest_framework import generics
from .models import Tournoi, Participant
from .serializers import TournoiSerializer, ParticipantSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render


@xframe_options_exempt
def bracket_view(request):
    # Utilisez la fonction de chargement de modèle Django pour charger votre modèle de page HTML
    template = loader.get_template('tcp_gaming/bracket/menu-bracket.html')
    context = {}  # Vous pouvez ajouter des données de contexte si nécessaire

    # Rendu du modèle avec les données de contexte
    rendered_template = template.render(context, request)

    # Créez une réponse HTTP à partir du modèle rendu
    response = HttpResponse(rendered_template, content_type='text/html')
    
    # Définissez les en-têtes pour autoriser l'inclusion depuis n'importe quel domaine
    response['X-Frame-Options'] = 'ALLOWALL'

    return response


@xframe_options_exempt
def bracket_single(request):
    # Utilisez la fonction de chargement de modèle Django pour charger votre modèle de page HTML
    template = loader.get_template('tcp_gaming/bracket/menu-single.html')
    context = {}  # Vous pouvez ajouter des données de contexte si nécessaire

    # Rendu du modèle avec les données de contexte
    rendered_template = template.render(context, request)

    # Créez une réponse HTTP à partir du modèle rendu
    response = HttpResponse(rendered_template, content_type='text/html')
    
    # Définissez les en-têtes pour autoriser l'inclusion depuis n'importe quel domaine
    response['X-Frame-Options'] = 'ALLOWALL'

    return response

class TournoiListCreate(generics.ListCreateAPIView):
    queryset = Tournoi.objects.all()
    serializer_class = TournoiSerializer

class ParticipantListCreate(generics.ListCreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class TournoiDelete(generics.DestroyAPIView):
    queryset = Tournoi.objects.all()
    serializer_class = TournoiSerializer

@api_view(['GET'])
def count_tournois(request):
    total_tournois = Tournoi.objects.count()
    return Response({'count': total_tournois})

from .models import Tournoi

def count_tournois_starting_with_single():
    # Utilisez le filtre de QuerySet pour obtenir les tournois dont le nom commence par "single"
    single_count = Tournoi.objects.filter(nom__startswith='single').count()
    return single_count
def count_single_tournois(request):
    single_count = count_tournois_starting_with_single()
    response_data = {'count': single_count}
    return JsonResponse(response_data)

def count_tournois_starting_with_double():
    # Utilisez le filtre de QuerySet pour obtenir les tournois dont le nom commence par "single"
    single_count = Tournoi.objects.filter(nom__startswith='double').count()
    return single_count

def count_double_tournois(request):
    double_count = count_tournois_starting_with_double()
    response_data = {'count': double_count}
    return JsonResponse(response_data)


def list_tournament(request):
    tournaments = Tournoi.objects.filter(nom__startswith='single')
    return render(request, 'tcp_gaming/bracket/menu-single.html', {'tournois': tournaments})

