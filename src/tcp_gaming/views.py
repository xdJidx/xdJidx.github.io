from datetime import datetime

from django.shortcuts import render


def index(request):

    date = datetime.today()

    return render(request, "tcp_gaming/index.html", context={"date": date})

def concours_view(request):
    return render(request, 'concours.html')

def photo_view(request):
    return render(request, 'photo.html')

def tournoi_view(request):
    return render(request, 'tournoi.html')

def autres_view(request):
    return render(request, 'autres.html')