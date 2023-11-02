from django.urls import path
from . import views

urlpatterns = [
    path('concours_list/', views.ConcoursListCreate.as_view(), name='concours-list'),
    path('participant_list/', views.ParticipantListCreate.as_view(), name='participant-list'),
]
