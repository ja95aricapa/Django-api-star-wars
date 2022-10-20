from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=50)
    birth_year = models.CharField(max_length=6)
    eye_color = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    hair_color = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    mass = models.CharField(max_length=20)
    skin_color = models.CharField(max_length=20)
    homeworld = models.CharField(max_length=50)
    films = models.JSONField()
    species = models.JSONField()
    starships = models.JSONField()
    vehicles = models.JSONField()
    url = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Planets(models.Model):
    name = models.CharField(max_length=50)
    diameter = models.CharField(max_length=50)
    rotation_period = models.CharField(max_length=50)
    orbital_period = models.CharField(max_length=50)
    gravity = models.CharField(max_length=50)
    population = models.CharField(max_length=50)
    climate = models.CharField(max_length=50)
    terrain = models.CharField(max_length=50)
    surface_water = models.CharField(max_length=50)
    residents = models.JSONField()
    films = models.JSONField()
    url = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Films(models.Model):
    title = models.CharField(max_length=50)
    episode_id = models.IntegerField()
    opening_crawl = models.TextField()
    director = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)
    release_date = models.DateField()
    species = models.JSONField()
    starships = models.JSONField()
    vehicles = models.JSONField()
    characters = models.JSONField()
    planets = models.JSONField()
    url = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title