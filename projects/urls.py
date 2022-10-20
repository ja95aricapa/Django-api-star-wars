from rest_framework import routers
from .api import PeopleViewSet, PlanetsViewSet, FilmsViewSet

router = routers.DefaultRouter()

router.register('api/people', PeopleViewSet, 'people')

#router.register(r'api/people', PeopleViewSet, 'people_search')

router.register('api/planets', PlanetsViewSet, 'planets')

router.register('api/films', FilmsViewSet, 'films')

urlpatterns = router.urls
