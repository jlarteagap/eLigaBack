from rest_framework import viewsets

from .models import Bboy, Crew, City
from .serializer import BboySerializer, CrewSerializer, CitySerializer

class BboyViewSet(viewsets.ModelViewSet):
    queryset = Bboy.objects.all()
    serializer_class = BboySerializer

class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CrewSerializer