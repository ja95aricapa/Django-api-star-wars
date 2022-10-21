from rest_framework import routers
from django.urls import path
from .api import PeopleViewSet, PlanetsViewSet, FilmsViewSet
from .views import login

router = routers.DefaultRouter()

router.register(prefix='people', viewset=PeopleViewSet, basename='people')
router.register(prefix='planets', viewset=PlanetsViewSet, basename='planets')
router.register(prefix='films', viewset=FilmsViewSet, basename='films')

urlpatterns = router.urls
