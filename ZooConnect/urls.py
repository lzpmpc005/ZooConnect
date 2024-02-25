
from django.contrib import admin
from django.urls import path
from DigitalZoo.views import add_species, edit_species, search_species, delete_species, add_venue, edit_venue, search_venue, delete_venue, add_animal, edit_animal, search_animal, delete_animal


urlpatterns = [
    path('admin/', admin.site.urls),

    path('add_species/', add_species, name='add_species'),
    path('edit_species/<int:species_id>/', edit_species, name='edit_species'),
    path('search_species/', search_species, name='search_species'),
    path('delete_species/<int:species_id>/', delete_species, name='delete_species'),

    path('add_venue/', add_venue, name='add_venue'),
    path('edit_venue/<int:venue_id>/', edit_venue, name='edit_venue'),
    path('search_venue/', search_venue, name='search_venue'),
    path('delete_venue/<int:venue_id>/', delete_venue, name='delete_venue'),

    path('add_animal/', add_animal, name='add_animal'),
    path('edit_animal/<int:animal_id>/', edit_animal, name='edit_animal'),
    path('search_animal/', search_animal, name='search_animal'),
    path('delete_animal/<int:animal_id>/', delete_animal, name='delete_animal'),
]
