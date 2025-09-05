from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('addCity/<str:city>/', addCity, name='addCity'),
    path('remove/<int:city_id>/', removeCity, name='removeCity'),
]
