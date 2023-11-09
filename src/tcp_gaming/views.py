from datetime import datetime
from django.shortcuts import render




def index(request):

    date = datetime.today()

    return render(request, "tcp_gaming/index.html", context={"date": date})

def concours_view(request):
    return render(request, "tcp_gaming/concours.html")

def photo_view(request):
    return render(request, "tcp_gaming/photo.html")

def tournoi_view(request):
    return render(request, "tcp_gaming/menu-bracket.html")

def autres_view(request):
    return render(request, "tcp_gaming/autres.html")


