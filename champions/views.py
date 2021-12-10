from rest_framework import generics
from .models import Champion
from .serializers import ChampionSerializer


class ChampionListView(generics.ListAPIView):
  queryset = Champion.objects.all()
  serializer_class = ChampionSerializer

class ChampionDetailView(generics.RetrieveAPIView):
  queryset = Champion.objects.all()
  serializer_class = ChampionSerializer
