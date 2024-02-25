from django.db import models

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
