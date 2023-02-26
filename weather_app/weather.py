''' The goal of this project is to create a weather app that shows the current weather conditions and forecast for a specific location.

Here are the steps you can take to create this project:

    Use the requests library to make an API call to a weather service (e.g. OpenWeatherMap) to retrieve the weather data for a specific location.

    Use the json library to parse the JSON data returned by the API call.

    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.

    Use the Pillow library to display the weather icons.

    Use the datetime library to display the current time and date. '''

import requests
from decouple import config
from datetime import datetime

'''This is backend of the code, which retrieves forecasts data from open weathermap.org. This data is used by UI part.
'''


def retrieve_coordinates(city_name):
    '''Retrieves coordinates for named city. Coordinates is used by below methods.
    '''
    response_location = requests.get(url='http://api.openweathermap.org/geo/1.0/direct', params={'q': city_name, 'appid': config('API_KEY')})
    json_response_location = response_location.json()
    lat = json_response_location[0]['lat']
    lon = json_response_location[0]['lon']
    return{'lat': lat, 'lon':lon}


def retrieve_recent_data(city_name):
    ''' Return recent weather data.
    '''
    coordinates = retrieve_coordinates(city_name)
    response_current = requests.get(url='https://api.openweathermap.org/data/2.5/weather', params={'lat': coordinates['lat'], 'lon': coordinates['lon'], 'appid': config('API_KEY'), 'units':'metric'})
    json_response_current = response_current.json()
    temperature = json_response_current['main']['temp']
    feels_like = json_response_current['main']['feels_like']
    description = json_response_current['weather'][0]['description']
    icon = json_response_current['weather'][0]['icon']
    return {'temperature': temperature, "feels_like" : feels_like, 'description': description, 'icon' : icon}


def find_how_much_hours_to_add():
    '''This code counts how much hours we should add to current time in order to receive forecast for tomorrow day - around 12 o clock. 
    It is needed as forecast service provides data for 3 hours interval.
    '''
    now = datetime.now()
    current_time = int(now.strftime("%H"))
    print("Current Time =", current_time)
    # this list is used to find out how much hours should be added to current time, to find time of midday of tomorrow.
    add_time_dict = {0:12, 3:11, 6:10, 9:9, 12:8, 15:7, 18:6, 21:5, 24:4}
    time_to_add = 0
    for time, add_time in add_time_dict.items():
        additional_time = time + 3 
        if time <= current_time < additional_time:
            time_to_add = add_time
            return time_to_add


def return_forecast(city_name):
    ''' Return data for weather forecast.
    '''
    hours_to_add = find_how_much_hours_to_add()
    coordinates = retrieve_coordinates(city_name)
    response_forecast = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params={'lat': coordinates['lat'], 'lon': coordinates['lon'], 'appid': config('API_KEY'), 'units':'metric'})
    json_response_current = response_forecast.json()
    temperature_day = json_response_current['list'][hours_to_add]['main']['temp_max']
    temperature_night = json_response_current['list'][hours_to_add]['main']['temp_min']
    feels_like = json_response_current['list'][hours_to_add]['main']['feels_like']
    description = json_response_current['list'][hours_to_add]['weather'][0]['description']
    icon = json_response_current['list'][hours_to_add]['weather'][0]['icon']
    return {'temperature_day' : temperature_day, 'temperature_night': temperature_night, 'feels_like' : feels_like, 'description' : description, 'id' : id, 'icon' : icon}

