from rest_framework import serializers
from .models import Planets, Films, People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('id', 'name', 'birth_year', 'eye_color', 'gender', 'hair_color', 'height', 'mass', 'skin_color', 'homeworld', 'films', 'species', 'starships', 'vehicles', 'url', 'created', 'edited')
        read_only_fields = ('id', 'created',)


class PlanetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planets
        fields = ('id', 'name', 'diameter', 'rotation_period', 'orbital_period', 'gravity', 'population', 'climate', 'terrain', 'surface_water', 'residents', 'films', 'url', 'created', 'edited')
        read_only_fields = ('id', 'created',)


class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = ('id', 'title', 'episode_id', 'opening_crawl', 'director', 'producer', 'release_date', 'species', 'starships', 'vehicles', 'characters', 'planets', 'url', 'created', 'edited')
        read_only_fields = ('id', 'created',)
