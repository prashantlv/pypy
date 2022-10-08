import os
import requests

city = input("Enter city :")
APP_ID = os.environ.get("APPID")
url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city,APP_ID)

res = requests.get(url)
data = res.json() 

# pprint(data) for printing in human readable formate json
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

#not complete
