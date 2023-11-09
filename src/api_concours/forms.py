from django import forms
from .models import Concours

class ConcoursForm(forms.ModelForm):
    class Meta:
        model = Concours
        fields = ['nom', 'theme', 'date_inscription_debut', 'date_inscription_fin', 'date_vote_debut', 'date_vote_fin', 'date_resultats']
