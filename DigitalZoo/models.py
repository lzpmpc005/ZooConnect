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
class Staff(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def _str_(self):
        return self.username


# zookeeper is inherited from staff
class Zookeeper(Staff):
    name = models.CharField(max_length=100)
    responsibility = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    def __str__(self):
        return self.name


# normally should be more tables (food, medicine, status, etc) related
# for simplifying only related to animal and zookeeper to track
class CareLog(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    zookeeper = models.ForeignKey(Zookeeper, on_delete=models.CASCADE)
    weight = models.IntegerField()
    temperature = models.FloatField()
    diet = models.CharField(max_length=100)
    medicine = models.CharField(max_length=100)
    date = models.DateField()
    def _str_(self):
        return f"CareLog {self.log_id} for Animal {self.animal_id}"
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
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    search_fields = ('username', 'password')
@admin.register(Zookeeper)
class ZookeeperAdmin(admin.ModelAdmin):
    list_display = ('username', 'password' , 'name', 'responsibility', 'qualification')
    search_fields = ('username', 'password', 'name' , 'responsibility', 'qualification')

@admin.register(CareLog)
class CareLogAdmin(admin.ModelAdmin):
    list_display = ('animal', 'zookeeper', 'weight', 'temperature', 'diet', 'medicine', 'date')
    search_fields = ('animal__name', 'zookeeper__username', 'weight', 'temperature', 'diet', 'medicine', 'date')



class Tour(models.Model):
    name = models.CharField(max_length=100)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    route = models.JSONField(default=dict)
    duration = models.JSONField(default=dict)
    activity = models.JSONField(default=dict)
    animal = models.JSONField(default=dict)
    
    def __str__(self):
        return self.name