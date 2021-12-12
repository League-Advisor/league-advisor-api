from django.urls import path
from .views import ChampionListView, ChampionDetailView

urlpatterns = [
  path('', ChampionListView.as_view(), name = 'champion_list'),
  path('<int:pk>', ChampionDetailView.as_view(), name = 'champion_detail')
]