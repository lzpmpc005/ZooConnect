
from django.contrib import admin
from django.urls import path
from DigitalZoo.views import sign_in,success_view,error_view,zookeeper_list,tourists_view,homepage_view,login_view,add_entity, edit_entity, search_entity, delete_entity

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('add_entity/', add_entity, name='add'),
    path('edit_entity/', edit_entity, name='edit'),
    path('search_entity/', search_entity, name='search'),
    path('delete_entity/', delete_entity, name='delete_entity'),
    path('homepage/', homepage_view, name='homepage'),
    path("tourists/", tourists_view, name="tourists"),
    path("zookeeper_list/", zookeeper_list, name="zookeeper"),
    path('success_view' , success_view, name='success'),
    path('error_view' , error_view, name='error'),
    path('sign_in/', sign_in, name='sign_in'),
    ]
