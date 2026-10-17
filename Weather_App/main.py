import requests

city = input ("Enter a city:")

geo_url = "https://geocoding-api.open-meteo.com/v1/search?name=" + city + "&count=1"
geo_data = requests.get(geo_url).json()
if "results" not in geo_data:
    print("city not found")
else:
    place = geo_data["results"][0]
    lat = place["latitude"]
    lon = place["longitude"]
    url = "https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&longitude=" + str(lon) + "&current=temperature_2m"
    data = requests.get(url).json()
    print("Weather in", place["name"])
    print("Country:", place["country"])
    print("Temperature:", data["current"]["temperature_2m"], "C")