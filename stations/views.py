from rest_framework import viewsets

from stations.models import Station
from stations.serializers import StationSerializer


class StationsViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
