from django.urls import path
from .views import TournoiListCreate, ParticipantListCreate
from . import views

urlpatterns = [
    path('tournois/', TournoiListCreate.as_view(), name='tournoi-list-create'),
    path('participants/', ParticipantListCreate.as_view(), name='participant-list-create'),
    path('count-tournois/', views.count_tournois, name='count-tournois'),
    path('tournois/<int:pk>/', views.TournoiDelete.as_view(), name='tournoi-delete'),
    path('count-single/', views.count_single_tournois, name='count-single-tournois'),
    path('count-double/', views.count_double_tournois, name='count-double-tournois'),
    path('list-tournois/', views.list_tournament, name='list-tournois'),
    path('get-user/', views.get_current_user, name='get-user'),
    path('tournament/<int:tournament_id>/', views.display_tournament_info, name='tournament-info'),

]
