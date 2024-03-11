
from django.contrib import admin
from django.urls import path
from DigitalZoo.views import (care_log_list, add_care_log, delete_care_log,sign_in,success_view,error_view,zookeeper_list,
                              tourists_view,homepage_view,login_view,add_entity, edit_entity, search_entity, delete_entity,
                              tour

                              )

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
    path('care_logs/', care_log_list, name='care_log_list'),
    path('care_logs/add/', add_care_log, name='add_care_log'),
    path('care_logs/delete/<int:care_log_id>/', delete_care_log, name='delete_care_log'),
    path('tour/', tour, name='tour'),
    ]
