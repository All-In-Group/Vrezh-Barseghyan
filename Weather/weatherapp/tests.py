# Create your tests here.
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8a8e8b25085fb1de4c10c0f61a51deb0'
r = requests.get(url.format("V")).json()
print(r)
