import requests
import os 
from datetime import datetime
import math



user_api = '92f435ad60597baccda828a73a292d4b'

# print(api_data)
location = "Dakar"
complete_api_link = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"

api_link = requests.get(complete_api_link)
api_data = api_link.json()
if api_data['cod'] == '404':
    msg ='Invalid City'
else:
    temp_city = math.ceil((api_data['main']['temp'])- 273.15)

    weather_desc = api_data['weather'][0]['description']

    humidity = api_data['main']['humidity']
    desc = f'Weather description {weather_desc}'
    loc = f"The temperature at {location} is : {temp_city}"
    hum = f'Humidity {humidity}'



