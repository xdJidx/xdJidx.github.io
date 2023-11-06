from django.db import models
from django.views.generic import DetailView

class Tournoi(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateField()
    lieu = models.CharField(max_length=100)
    limite_joueurs = models.PositiveIntegerField(default=8)
    # Ajoutez d'autres champs si nécessaire

class Participant(models.Model):
    nom = models.CharField(max_length=100)
    tournoi = models.ForeignKey(Tournoi, related_name='participants', on_delete=models.CASCADE)


