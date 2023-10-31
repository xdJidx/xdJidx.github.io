from django.db import models
from django.contrib.auth.models import User

class Concours(models.Model):
    nom = models.CharField(max_length=100)
    date_debut = models.DateTimeField()
    date_fin_inscription = models.DateTimeField()
    date_fin_votes = models.DateTimeField()

class Inscription(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    concours = models.ForeignKey(Concours, on_delete=models.CASCADE)
    pseudo = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    est_validee = models.BooleanField(default=False)

class Vote(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    inscription = models.ForeignKey(Inscription, on_delete=models.CASCADE)

class Resultat(models.Model):
    concours = models.ForeignKey(Concours, on_delete=models.CASCADE)
    gagnant = models.ForeignKey(User, on_delete=models.CASCADE)
    date_gagnant = models.DateTimeField()

class Participant(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name