
from django.contrib import admin
from django.urls import path
from DigitalZoo.views import homepage_view,login_view,add_entity, edit_entity, search_entity, delete_entity

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('add_entity/', add_entity, name='add'),
    path('edit_entity/', edit_entity, name='edit'),
    path('search_entity/', search_entity, name='search'),
    path('delete_entity/', delete_entity, name='delete_entity'),
    path('homepage/', homepage_view, name='homepage'),

    ]
