from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import ConcoursForm
from rest_framework import generics

@login_required
class CreerConcours(generics.ListCreateAPIView):
    template_name = 'creer_concours.html'

    def get(self, request):
        form = ConcoursForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ConcoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_concours')  # Rediriger vers la liste des concours après la création
        return render(request, self.template_name, {'form': form})
