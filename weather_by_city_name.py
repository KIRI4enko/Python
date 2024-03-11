'''
Погода по названию города
Weather by city name
'''
def Deg(grad: int):
    res = ''
    if 0 <= grad <= 30 or 330 <= grad <= 360:
        res = 'Северный'
    elif 30 < grad < 60:
        res = 'Северо-Восточный'
    elif 60 <= grad <= 120:
        res = 'Восточный'
    elif 120 <= grad <= 150:
        res = 'Юго-Восточный'
    elif 150 < grad < 210:
        res = "Южный"
    elif 210 <= grad <= 240:
        res = "Юго-Западный"
    elif 240 < grad < 300:
        res = 'Западный'
    elif 300 <= grad < 330:
        res = "Северо-Западный"
    return res

import requests
import json

city = input('Введите город: ')
url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid=eb455c3ca80dc6c8d0078171ff5cab0b"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

if response:
    data_city = json.loads(response.content)
    if len(data_city):
        city = data_city[0]['name']
        lat = data_city[0]['lat']
        lon = data_city[0]['lon']
        weather_ulr = f'https://api.openweathermap.org/data/2.5/weather?lang=ru&lat={lat}&lon={lon}&appid=eb455c3ca80dc6c8d0078171ff5cab0b&units=metric'
        response_weather = requests.get(weather_ulr)
        if response_weather:
            data_weather = json.loads(response_weather.content)
            temp = data_weather['main']['temp']
            wind_speed = data_weather['wind']['speed']
            wind_deg = data_weather['wind']['deg']
            description = data_weather['weather'][0]['description']
            print(f'Температура в г.{city} {temp} градусов Цельсия, ветер {Deg(wind_deg)}, скорость {wind_speed} м/с, {description}')

        else:
            print('Погода не найдена', response_weather.status_code)
    else:
        print('Город не найден', city)
else:
    print('ERROR', response.status_code)


