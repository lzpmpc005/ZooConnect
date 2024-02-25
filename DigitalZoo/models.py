from django.db import models
from django.http import JsonResponse
from django.contrib import admin
class Species(models.Model):
    name = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    light_intensity = models.IntegerField()

    def __str__(self):
        return self.name
    
class Venue(models.Model):
    name = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    size = models.IntegerField()
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    light_intensity = models.IntegerField()
    
    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    diet = models.CharField(max_length=100)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'habitat', 'temperature', 'humidity', 'light_intensity')
    search_fields = ('name', 'habitat')

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'habitat', 'location', 'size', 'temperature', 'humidity', 'light_intensity')
    search_fields = ('name', 'habitat', 'location')

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'diet', 'species', 'venue')
    search_fields = ('name', 'diet', 'species__name', 'venue__name')