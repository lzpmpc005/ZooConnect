from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Venue, Animal, Species
from .models import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('homepage')  # Redirect to the homepage
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
from django.shortcuts import render

def homepage_view(request):
    return render(request, 'homepage.html')


@csrf_exempt
def add_entity(request):
    if request.method == "GET":

        species_list = Species.objects.all()
        venues_list = Venue.objects.all()
        return render(request, 'add.html', {"species_list": species_list, "venues_list": venues_list})

    elif request.method == 'POST':

        data = json.loads(request.body)
        entity_type = data.get('entity_type')

        if entity_type == 'species':

            name = data.get('name')
            habitat = data.get('habitat')
            temperature = data.get('temperature')
            humidity = data.get('humidity')
            light_intensity = data.get('light_intensity')
            Species.objects.create(name=name, habitat=habitat, temperature=temperature, humidity=humidity, light_intensity=light_intensity)
            return JsonResponse({'message': 'Species added successfully'}, status=201)

        elif entity_type == 'animal':

            name = data.get('name')
            age = data.get('age')
            diet = data.get('diet')
            species_id = data.get('species_id')  # 提取物种 ID
            venue_id = data.get('venue_id')  # 提取场地 ID
            species = Species.objects.get(pk=species_id)
            venue = Venue.objects.get(pk=venue_id)
            Animal.objects.create(name=name, age=age, diet=diet, species=species, venue=venue)
            return JsonResponse({'message': 'Animal added successfully'}, status=201)

        elif entity_type == 'venue':

            name = data.get('name')
            habitat = data.get('habitat')
            location = data.get('location')
            size = data.get('size')
            temperature = data.get('temperature')
            humidity = data.get('humidity')
            light_intensity = data.get('light_intensity')
            Venue.objects.create(name=name, habitat=habitat, location=location, size=size, temperature=temperature, humidity=humidity, light_intensity=light_intensity)
            return JsonResponse({'message': 'Venue added successfully'}, status=201)

        else:

            return JsonResponse({'error': 'Invalid entity type'}, status=400)

    else:

        return JsonResponse({'error': 'Only GET and POST requests are allowed'}, status=400)


def delete_entity(request):
    if request.method == 'GET':
        species_list = Species.objects.all()
        animal_list = Animal.objects.all()
        venue_list = Venue.objects.all()
        return render(request, 'delete.html', {'species_list': species_list, 'animal_list': animal_list, 'venue_list': venue_list})
    elif request.method == 'POST':
        entity_type = request.POST.get('entity_type')
        entity_id = request.POST.get('entity_id')
        if entity_type == 'species':
            try:
                species = Species.objects.get(pk=entity_id)
                species.delete()
                return JsonResponse({'message': 'Species deleted successfully'})
            except Species.DoesNotExist:
                return JsonResponse({'error': 'Species does not exist'}, status=404)
        elif entity_type == 'animal':
            try:
                animal = Animal.objects.get(pk=entity_id)
                animal.delete()
                return JsonResponse({'message': 'Animal deleted successfully'})
            except Animal.DoesNotExist:
                return JsonResponse({'error': 'Animal does not exist'}, status=404)
        elif entity_type == 'venue':
            try:
                venue = Venue.objects.get(pk=entity_id)
                venue.delete()
                return JsonResponse({'message': 'Venue deleted successfully'})
            except Venue.DoesNotExist:
                return JsonResponse({'error': 'Venue does not exist'}, status=404)
        else:
            return JsonResponse({'error': 'Invalid entity type'}, status=400)


from django.shortcuts import render
from django.http import JsonResponse
from .models import Species, Animal, Venue
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def search_entity(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        if not keyword:
            species = Species.objects.all()
            animals = Animal.objects.all()
            venues = Venue.objects.all()
        else:
            species = Species.objects.filter(name__icontains=keyword)
            animals = Animal.objects.filter(name__icontains=keyword)
            venues = Venue.objects.filter(name__icontains=keyword)

        data = {
            'species': [{'name': s.name} for s in species],
            'animals': [{'name': a.name} for a in animals],
            'venues': [{'name': v.name} for v in venues]
        }

        return render(request, 'search.html', data)

    elif request.method == 'POST':
        data = json.loads(request.body)
        keyword = data.get('keyword')
        if keyword:
            species = Species.objects.filter(name__icontains=keyword)
            animals = Animal.objects.filter(name__icontains=keyword)
            venues = Venue.objects.filter(name__icontains=keyword)

            data = {
                'species': [{'name': s.name} for s in species],
                'animals': [{'name': a.name} for a in animals],
                'venues': [{'name': v.name} for v in venues]
            }

            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'error': 'No keyword provided for search'}, status=400)

    return JsonResponse({'error': 'Only GET and POST requests are allowed'}, status=400)

@csrf_exempt
def edit_entity(request):
    if request.method == 'GET':
        venues = Venue.objects.all()
        animals = Animal.objects.all()
        species = Species.objects.all()
        context = {
            'venues': venues,
            'animals': animals,
            'species': species,
        }
        return render(request, 'edit.html', context)

    elif request.method == 'POST':
        data = json.loads(request.body)
        entity_type = data.get('entity_type')
        entity_id = data.get('entity_id')
        if entity_type == 'species':
            try:
                species = Species.objects.get(pk=entity_id)
                species.name = data.get('name', species.name)
                species.habitat = data.get('habitat', species.habitat)
                species.temperature = data.get('temperature', species.temperature)
                species.humidity = data.get('humidity', species.humidity)
                species.light_intensity = data.get('light_intensity', species.light_intensity)
                species.save()
                return JsonResponse({'message': 'Species updated successfully'})
            except Species.DoesNotExist:
                return JsonResponse({'error': 'Species does not exist'}, status=404)
        elif entity_type == 'animal':
            try:
                animal = Animal.objects.get(pk=entity_id)
                animal.name = data.get('name', animal.name)
                animal.age = data.get('age', animal.age)
                animal.diet = data.get('diet', animal.diet)
                # Assuming species and venue are foreign keys in Animal model
                animal.species_id = data.get('species_id', animal.species_id)
                animal.venue_id = data.get('venue_id', animal.venue_id)
                animal.save()
                return JsonResponse({'message': 'Animal updated successfully'})
            except Animal.DoesNotExist:
                return JsonResponse({'error': 'Animal does not exist'}, status=404)
        elif entity_type == 'venue':
            try:
                venue = Venue.objects.get(pk=entity_id)
                venue.name = data.get('name', venue.name)
                venue.habitat = data.get('habitat', venue.habitat)
                venue.location = data.get('location', venue.location)
                venue.size = data.get('size', venue.size)
                venue.temperature = data.get('temperature', venue.temperature)
                venue.humidity = data.get('humidity', venue.humidity)
                venue.light_intensity = data.get('light_intensity', venue.light_intensity)
                venue.save()
                return JsonResponse({'message': 'Venue updated successfully'})
            except Venue.DoesNotExist:
                return JsonResponse({'error': 'Venue does not exist'}, status=404)
        else:
            return JsonResponse({'error': 'Invalid entity type'}, status=400)
    else:
        return JsonResponse({'error': 'Only GET and POST requests are allowed'}, status=400)
