import json,requests


API_KEY = '125586a42d0bd62391a4b2c4b3c59057'


#get city name and 2-letter counter_code 
print("Enter City Name and 2-letter country code ( Ex. san francisco us")
city_name = input(': ')
country_code = city_name[-2:]

#request URL 
url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name[:-3]},{country_code}&appid={API_KEY}"

#make a request to API
res = requests.get(url)
res.raise_for_status()

data = res.text
weatherDATA = json.loads(data)
# pprint.pprint(weatherDATA)

wthr = weatherDATA['list']

print()
print(f"Current weather from {city_name[:-3]},{country_code}")
print(f"Weather: {wthr[0]['weather'][0]['main']} - Description: {wthr[0]['weather'][0]['description']}")
print()
print("Tomorrow")
print(f"Weather: {wthr[4]['weather'][0]['main']} - Description: {wthr[4]['weather'][0]['description']}")
print()
print("The Day After Tomorrow")
print(f"Weather: {wthr[12]['weather'][0]['main']} - Description: {wthr[12]['weather'][0]['description']}")