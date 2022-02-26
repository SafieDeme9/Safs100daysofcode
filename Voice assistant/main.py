import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from joke import jokes
import requests 
import math
import random

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
user_api = '92f435ad60597baccda828a73a292d4b'

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sophia' in command:
                command = command.replace('sophia', '')
                print(command)
    except:
        print("Error")
    return command

def weather():
    location = command.replace('weather at', '')
    complete_api_link = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    if api_data['cod'] == '404':
        msg ='Invalid City'
        talk(msg)
    else:
        temp_city = math.ceil((api_data['main']['temp'])- 273.15)

        weather_desc = api_data['weather'][0]['description']

        humidity = api_data['main']['humidity']
        desc = f'Weather description {weather_desc} '
        loc = f"The temperature at {location} is : {temp_city} "
        hum = f'Humidity {humidity} '
        text = desc + loc + hum
        print(text)
        talk(text)


while True:
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(random.choice(jokes))
    elif 'weather at' in command:
        weather()
    else:
        talk('Please say the command again.')

