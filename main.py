import requests

key = 'здесь ваш ключ'
url = 'http://api.openweathermap.org/data/2.5/weather'
params = {'APPID': key, 'q': 'Москва', 'units': 'metric'}

response = requests.get(url, params=params)
result = response.json()

print(result)
print(result['main']['temp'])
