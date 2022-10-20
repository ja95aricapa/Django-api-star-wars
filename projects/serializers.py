from rest_framework import serializers
from .models import Planets, Films, People

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'
        read_only_fields = ('id', 'created',)


class PlanetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planets
        fields = '__all__'
        read_only_fields = ('id', 'created',)


class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = '__all__'
        read_only_fields = ('id', 'created',)
