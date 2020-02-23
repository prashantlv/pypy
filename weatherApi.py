import requests
from pprint import pprint

city = input("Enter city :")
url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid=070870a3f63e0378bdd30bd70f20bce5'.format(city)

res = requests.get(url)     # request data from url thr request obj
data = res.json()           # store json data in py dictonary

# pprint(data)
name = data['name']
humidity = data['main']['humidity']
pressure = data['main']['pressure']
temp = data['main']['temp']
desc = data['weather'][0]['description']
windSpeed = data['wind']['speed']

print('Name of city :',name)
print('Humidity is :',humidity)
print('Air Pressure is :',pressure)
print('Temperature is :',temp)
print('Wind Speed is  :',windSpeed)
print('Description :',desc)


# api from https://home.openweathermap.org/