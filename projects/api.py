from .models import Planets, Films, People
from rest_framework import viewsets, permissions
from .serializers import PeopleSerializer, PlanetsSerializer, FilmsSerializer
from .filters import NameFilterBackend



class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    name = 'people'
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PeopleSerializer
    filter_backends = (NameFilterBackend,)


class PlanetsViewSet(viewsets.ModelViewSet):
    queryset = Planets.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PlanetsSerializer


class FilmsViewSet(viewsets.ModelViewSet):
    queryset = Films.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = FilmsSerializer
