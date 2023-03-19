from django.shortcuts import render
from django.http import HttpResponse
import datetime
import requests

def index(request):
    try:
        # checking if the method is POST
        if request.method == 'POST':
            poststatus = True
            API_KEY = '15edf62985d1cc636d5b71fef41aa3e9'
            # getting the city name from the form input
            city_name = request.POST.get('cityname')
            print(city_name)
            # the url for current weather, takes city_name and API_KEY
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            # converting the request response to json
            response = requests.get(url).json()
            print(response)
            # getting the current time
            current_time = datetime.datetime.now()
            # formatting the time using directives, it will take this format Day, Month Date Year, Current Time
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
            # bundling the weather information in one dictionary
            city_weather_update = {
                'city': city_name,
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
                'country_code': response['sys']['country'],
                'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                'time': formatted_time,
                'check': poststatus,
            }
        # if the request method is GET, empty the dictionary
        else:
            city_weather_update = {}
        context = {'city_weather_update': city_weather_update}
        return render(request, 'home.html', context)
    # if there is an error, render the 404 page
    except Exception as e:
        print(e)
        return render(request, '404.html')
