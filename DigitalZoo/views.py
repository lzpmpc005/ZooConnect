from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Venue, Animal, Species
from .models import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random

def homepage(request):
    return render(request, 'homepage.html')

def staff_login_in(request):
    return render(request, 'login_in.html')

def animal_management(request):
    return render(request, 'animalmanagement.html')

def animal_addition(request):
    return render(request, 'add_animal.html')

def animal_deletion(request):
    return render(request, 'delete_animal.html')

def animal_edition(request):
    return render(request, 'update_animal.html')

def animal_search(request):
    return render(request, 'search_animal.html')

@csrf_exempt
def add_species(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        habitat = data.get('habitat')
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        light_intensity = data.get('light_intensity')
        species = Species.objects.create(
            name=name, 
            habitat=habitat, 
            temperature=temperature, 
            humidity=humidity, 
            light_intensity=light_intensity
        )
        return JsonResponse({'message': 'Species added successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=400)

@csrf_exempt
def add_animal(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        age = int(data.get('age'))
        diet = data.get('diet')
        species = int(data.get('species'))
        venue = int(data.get('venue'))
        animals = Animal.objects.create(
            name=name, 
            age=age, 
            diet=diet,
            species_id=species,
            venue_id=venue
        )
        return JsonResponse({'message': 'Animal added successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=400)

@csrf_exempt
def add_venue(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        habitat = data.get('habitat')
        location = data.get('location')
        size = data.get('size')
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        light_intensity = data.get('light_intensity')
        venue = Venue.objects.create(
            name=name,
            habitat=habitat,
            location=location,
            size=size,
            temperature=temperature,
            humidity=humidity,
            light_intensity=light_intensity
        )
        return JsonResponse({'message': 'Venue added successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=400)

@csrf_exempt
def edit_species(request, species_id):
    try:
        species = Species.objects.get(pk=species_id)
    except Species.DoesNotExist:
        return JsonResponse({'error': 'Species does not exist'}, status=404)
    if request.method == 'PUT':
        data = json.loads(request.body)
        species.name = data.get('name', species.name)
        species.habitat = data.get('habitat', species.habitat)
        species.temperature = data.get('temperature', species.temperature)
        species.humidity = data.get('humidity', species.humidity)
        species.light_intensity = data.get('light_intensity', species.light_intensity)
        species.save()
        return JsonResponse({'message': 'Species updated successfully'})
    else:
        return JsonResponse({'error': 'Only PUT requests are allowed'}, status=400)

def edit_animal(request, animal_id):
    if request.method == 'PUT':
        try:
            animal = Animal.objects.get(pk=animal_id)
        except Animal.DoesNotExist:
            return JsonResponse({'error': 'Animal does not exist'}, status=404)

        data = json.loads(request.body)
        animal.name = data.get('name', animal.name)
        animal.age = int(data.get('age', animal.age))
        animal.diet = data.get('diet', animal.diet)
        animal.species_id = int(data.get('species', animal.species))
        animal.venue_id = int(data.get('venue', animal.venue))
        animal.save()
        return JsonResponse({'message': 'Animal updated successfully'})
    else:
        return JsonResponse({'error': 'Only PUT requests are allowed'}, status=400)

def edit_venue(request, venue_id):
    try:
        venue = Venue.objects.get(pk=venue_id)
    except Venue.DoesNotExist:
        return JsonResponse({'error': 'Venue does not exist'}, status=404)
    if request.method == 'PUT':
        data = json.loads(request.body)
        venue.name = data.get('name', venue.name)
        venue.habitat = data.get('habitat', venue.habitat)
        venue.location = data.get('location', venue.location)
        venue.size = data.get('size', venue.size)
        venue.temperature = data.get('temperature', venue.temperature)
        venue.humidity = data.get('humidity', venue.humidity)
        venue.light_intensity = data.get('light_intensity', venue.light_intensity)
        venue.save()
        return JsonResponse({'message': 'Venue updated successfully'})
    else:
        return JsonResponse({'error': 'Only PUT requests are allowed'}, status=400)




def search_species(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        species = Species.objects.filter(name__icontains=keyword)
        data = [{'name': s.name, 'habitat': s.habitat, 'temperature': s.temperature, 'humidity': s.humidity, 'light_intensity': s.light_intensity} for s in species]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=400)

def search_animal(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        if not keyword:
            return JsonResponse({'error': 'Please provide a search keyword'}, status=400)
        try:
            animals = Animal.objects.filter(name__icontains=keyword)
            data = [{'name': a.name, 'age': a.age, 'diet': a.diet, 'species': a.species.name, 'venue': a.venue.name} for a in animals]
            return JsonResponse(data, safe=False)
        except Animal.DoesNotExist:
            return JsonResponse({'error': 'Animal does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=400)

def search_venue(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        venues = Venue.objects.filter(name__icontains=keyword)
        data = [{'name': v.name, 'habitat': v.habitat, 'location': v.location, 'size': v.size, 'temperature': v.temperature, 'humidity': v.humidity, 'light_intensity': v.light_intensity} for v in venues]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=400)

@csrf_exempt
def delete_animal(request, animal_id):
    if request.method == 'DELETE':
            try:
                animal = Animal.objects.get(pk=animal_id)
                animal.delete()
                return JsonResponse({'message': 'Animal deleted successfully'})
            except Animal.DoesNotExist:
                return JsonResponse({'error': 'Animal does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Only DELETE requests are allowed'}, status=400)
    

def delete_venue(request, venue_id):
    try:
        venue = Venue.objects.get(pk=venue_id)
    except Venue.DoesNotExist:
        return JsonResponse({'error': 'Venue does not exist'}, status=404)

    if request.method == 'DELETE':
        venue.delete()
        return JsonResponse({'message': 'Venue deleted successfully'})
    else:
        return JsonResponse({'error': 'Only DELETE requests are allowed'}, status=400)


def delete_species(request, species_id):
    try:
        species = Species.objects.get(pk=species_id)
    except Species.DoesNotExist:
        return JsonResponse({'error': 'Species does not exist'}, status=404)

    if request.method == 'DELETE':
        species.delete()
        return JsonResponse({'message': 'Species deleted successfully'})
    else:
        return JsonResponse({'error': 'Only DELETE requests are allowed'}, status=400)


