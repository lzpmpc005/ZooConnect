from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Venue, Animal, Species,Zookeeper
from .models import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
from django.contrib.auth import authenticate, login as auth_login
from .models import Animal
from .models import CareLog
from .forms import CareLogForm

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


def tourists_view(request):
    animals = Animal.objects.all()
    ages = [a.age for a in animals]
    diets = [a.diet for a in animals]
    species = [a.species.name for a in animals]

    context = {
        "animals": animals,
        "ages": ages,
        "diets": diets,
        "species": species,
    }
    return render(request, 'tourists.html', context)



def homepage_view(request):
    animals = Animal.objects.all()
    ages = [a.age for a in animals]
    diets = [a.diet for a in animals]
    species = [a.species.name for a in animals]
    venues = Venue.objects.all()
    zookeepers = Zookeeper.objects.all()
    care_logs = CareLog.objects.all()
    context = {
        "animals": animals,
        "ages": ages,
        "diets": diets,
        "species": species,
        "venues": venues,
        "zookeepers": zookeepers,
        "care_logs": care_logs,
    }
    return render(request, 'homepage.html', context)

def success_view(request):
    return render(request, 'success.html')
def error_view(request):
    return render(request, 'error.html')
def sign_in(request):
    return render(request, 'sign_in.html')
@csrf_exempt
def add_entity(request):
    if request.method == "GET":
        animal_list = Animal.objects.all()
        species_list = Species.objects.all()
        venue_list = Venue.objects.all()
        zookeeper_list = Zookeeper.objects.all()
        return render(request, 'add.html', {"species_list": species_list, "venue_list": venue_list, 'animal_list': animal_list, 'zookeeper_list': zookeeper_list})

    elif request.method == 'POST':
        entity_type = request.POST.get('entity_type')

        if entity_type == 'species':
            name = request.POST.get('name')
            habitat = request.POST.get('habitat')
            temperature = request.POST.get('temperature')
            humidity = request.POST.get('humidity')
            light_intensity = request.POST.get('light_intensity')
            Species.objects.create(name=name, habitat=habitat, temperature=temperature, humidity=humidity, light_intensity=light_intensity)
            return redirect('success')  # Redirect to success page

        elif entity_type == 'animal':
            name = request.POST.get('name')
            age = request.POST.get('age')
            diet = request.POST.get('diet')
            species_id = request.POST.get('species_id')
            venue_id = request.POST.get('venue_id')
            species = Species.objects.get(pk=species_id)
            venue = Venue.objects.get(pk=venue_id)
            Animal.objects.create(name=name, age=age, diet=diet, species=species, venue=venue)
            return redirect('success')

        elif entity_type == 'venue':
            name = request.POST.get('name')
            habitat = request.POST.get('habitat')
            location = request.POST.get('location')
            size = request.POST.get('size')
            temperature = request.POST.get('temperature')
            humidity = request.POST.get('humidity')
            light_intensity = request.POST.get('light_intensity')
            Venue.objects.create(name=name, habitat=habitat, location=location, size=size, temperature=temperature, humidity=humidity, light_intensity=light_intensity)
            return redirect('success')

        elif entity_type == "zookeeper":
            name = request.POST.get('name')
            qualification = request.POST.get('qualification')
            responsibility = request.POST.get('responsibility')
            venue_id = request.POST.get('venue_id')
            Zookeeper.objects.create(name=name, qualification=qualification, responsibility=responsibility)
            return redirect('success')

        elif entity_type == "carelog":
            animal_id = request.POST.get('animal_id')
            zookeeper_id = request.POST.get('zookeeper_id')
            animal = Animal.objects.get(pk=animal_id)
            zookeeper = Zookeeper.objects.get(pk=zookeeper_id)
            CareLog.objects.create(animal=animal, zookeeper=zookeeper)
            return redirect('success')
        else:
            return render(request, 'error.html', {'error': 'Invalid entity type'})

    else:
        return render(request, 'error.html', {'error': 'Only GET and POST requests are allowed'})
# 删除实体的视图函数
def delete_entity(request):
    if request.method == 'GET':
        # 获取所有的物种、动物和场馆列表
        species_list = Species.objects.all()
        animal_list = Animal.objects.all()
        venue_list = Venue.objects.all()
        return render(request, 'delete.html', {'species_list': species_list, 'animal_list': animal_list, 'venue_list': venue_list})
    elif request.method == 'POST':
        entity_type = request.POST.get('delete_type')  # 获取要删除的实体类型
        entity_id = request.POST.get('entity_id')  # 获取要删除的实体ID

        # 根据实体类型执行相应的删除操作
        if entity_type == 'species':
            try:
                species = Species.objects.get(pk=entity_id)
                species.delete()
                return render(request, 'success.html', {'message': 'Species deleted successfully'})
            except Species.DoesNotExist:
                return render(request, 'error.html', {'error': 'Species does not exist'}, status=404)
        elif entity_type == 'animal':
            try:
                animal = Animal.objects.get(pk=entity_id)
                animal.delete()
                return render(request, 'success.html', {'message': 'Animal deleted successfully'})
            except Animal.DoesNotExist:
                return render(request, 'error.html', {'error': 'Animal does not exist'}, status=404)
        elif entity_type == 'venue':
            try:
                venue = Venue.objects.get(pk=entity_id)
                venue.delete()
                return render(request, 'success.html', {'message': 'Venue deleted successfully'})
            except Venue.DoesNotExist:
                return render(request, 'error.html', {'error': 'Venue does not exist'}, status=404)
        else:
            return render(request, 'error.html', {'error': 'Invalid entity type'}, status=400)



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
        elif entity_type == "zookeeper":
            try:
                zookeeper = Zookeeper.objects.get(pk=entity_id)
                zookeeper.name = data.get('name', zookeeper.name)
                zookeeper.age = data.get('age', zookeeper.age)
                zookeeper.diet = data.get('diet', zookeeper.diet)
                # Assuming species and venue are foreign keys in Zookeeper model
                zookeeper.species_id = data.get('species_id', zookeeper.species_id)
                zookeeper.venue_id = data.get('venue_id', zookeeper.venue_id)
                zookeeper.save()
                return JsonResponse({'message': 'Zookeeper updated successfully'})
            except Zookeeper.DoesNotExist:
                return JsonResponse({'error': 'Zookeeper does not exist'}, status=404)
        elif entity_type == "carelog":
            try:
                carelog = CareLog.objects.get(pk=entity_id)
                carelog.animal_id = data.get('animal_id', carelog.animal_id)
                carelog.zookeeper_id = data.get('zookeeper_id', carelog.zookeeper_id)
                carelog.save()
                return JsonResponse({'message': 'Care log updated successfully'})
            except CareLog.DoesNotExist:
                return JsonResponse({'error': 'Care log does not exist'}, status=404)
        else:
            return JsonResponse({'error': 'Invalid entity type'}, status=400)
    else:
        return JsonResponse({'error': 'Only GET and POST requests are allowed'}, status=400)
def staff_list(request):
    staff_members = User.objects.filter(is_staff=True)
    context = {'staff_members': staff_members}
    return render(request, 'staff_list.html', context)

def zookeeper_list(request):
    zookeepers = Zookeeper.objects.all()
    context = {'zookeepers': zookeepers}
    return render(request, 'zookeeper_list.html', context)

def add_care_log(request):
    if request.method == 'POST':
        form = CareLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('care_log_list')
    else:
        form = CareLogForm()
    return render(request, 'add_care_log.html', {'form': form})

def delete_care_log(request, care_log_id):
    care_log = CareLog.objects.get(pk=care_log_id)
    care_log.delete()
    return redirect('care_log_list')
def care_log_list(request):
    care_logs = CareLog.objects.all()
    return render(request, 'care_log_list.html', {'care_logs': care_logs})


def delete_animal(request, animal_id):
    try:
        animal = Animal.objects.get(pk=animal_id)
        animal.delete()
        return redirect('animal_list')  # Redirect to the animal list page after deletion
    except Animal.DoesNotExist:
        return redirect('animal_list')  # Redirect to the animal list page if the animal does not exist