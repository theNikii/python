#Задание 2. Работа с параметрами запроса
#1. Используйте API OpenWeather для получения данных о погоде.
#2. Напишите программу, которая:
# принимает название города от пользователя,
# отправляет GET-запрос к API и выводит текущую температуру и
#описание погоды.
import requests


api_key = '8f29a6228878aa437cb1acad545cd601'
city = 'Липецк'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
response = requests.get(url)


if response.status_code == 200:
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']

    print(f"Текущая температура в {city}: {temperature}°C")
    print(f"Описание погоды: {description}")