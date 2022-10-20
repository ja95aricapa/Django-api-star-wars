from .models import Planets, Films, People
from rest_framework import viewsets, permissions
from .serializers import PeopleSerializer, PlanetsSerializer, FilmsSerializer

class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PeopleSerializer

    def get_queryset(self):
        queryset = People.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset


class PlanetsViewSet(viewsets.ModelViewSet):
    queryset = Planets.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PlanetsSerializer


class FilmsViewSet(viewsets.ModelViewSet):
    queryset = Films.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FilmsSerializer