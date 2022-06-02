from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('home/', home, name="home"),
    # Home
    path('', index, name='index'),
    path('selcircle/', selcircle, name='selcircle'),
    path('feedback/', index, name='feedback'),
    path('searchbycircle/', index, name='searchbycircle'),
    path('searchbyssa', index, name='searchbyssa'),
    path('searchsingle/', index, name='searchsingle'),   
]