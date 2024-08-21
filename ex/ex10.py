import requests
city_name='울산'
API_key='35e36e0bb5258a226356467f40324896'
limit=5
url =f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_key}'
res=requests.get(url)
data=res.json()
print(len(data))
lat=data[0]['lat']
lon=data[0]['lon']
print(lat,lon)
url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
res=requests.get(url)
weather=res.json()
print(weather)
print('\n')
print(weather['weather'][0]['description'])
print(weather['weather'][10]['temp'])
print('20307 김해람')