import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import HotPlace

API_KEY = "7191c4d35154475ac50a5a8758a52088"

def home(request):
    weather_data = {}
    
    if request.method == 'POST':
        city = request.POST.get('city')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
        response = requests.get(url).json()

        if response.get('cod') == 200:
            weather_data = {
                "city": city,
                "temp": round(response['main']['temp'] - 273.15, 2),
                "description": response['weather'][0]['description'],
                "icon": response['weather'][0]['icon'],
            }
        else:
            weather_data = {"error": "City not found!"}
    elif request.method == 'GET':
        weather_data = {
            "city": 'City',
            "temp": 'Temprature',
            "description": 'weather description',
            "icon": '01d',
        }


    hot_places = []
    for place in HotPlace.objects.all():
        url = f'https://api.openweathermap.org/data/2.5/weather?q={place.city}&appid={API_KEY}'
        res = requests.get(url).json()
        if res.get("cod") == 200:
            hot_places.append({
                'id': place.id,
                "city": place.city,
                "temp": round(res["main"]["temp"] - 273.15, 2),
                "description": res["weather"][0]["description"],
                "icon": res["weather"][0]["icon"],
            })

    return render(request, "home.html", {
        "weather_data": weather_data,
        "hot_places": hot_places
    })


def addCity(request, city):
    """Add a city to Hot Places"""
    HotPlace.objects.get_or_create(city=city)
    return redirect("home")

def removeCity(request, city_id):
    place = get_object_or_404(HotPlace, id=city_id)
    place.delete()
    return redirect('home')