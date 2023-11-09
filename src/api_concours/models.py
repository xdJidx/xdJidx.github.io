from django.db import models

class Concours(models.Model):
    nom = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    date_inscription_debut = models.DateTimeField()
    date_inscription_fin = models.DateTimeField()
    date_vote_debut = models.DateTimeField()
    date_vote_fin = models.DateTimeField()
    date_resultats = models.DateTimeField()
