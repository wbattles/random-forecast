import requests
import random
import pandas as pd

headers = {
    "User-Agent": "Weather Test App",
    "Accept": "application/ld+json"
}

def getCords():
    num = random.randrange(1000)
    cities = pd.read_csv("cordinates.csv")

    city = cities.iloc[[num]]

    lat = float(city["lat"])
    lon = float(city["lon"])
    # lat = 36.1539816
    # lon = -95.992775

    return f"{lat},{lon}"

def getEndpoint(cordinates):
    city_cords =  cordinates
    url = f"https://api.weather.gov/points/{city_cords}"


    city_station_data = requests.get(url, headers=headers)
    city_data = city_station_data.json()
    forecast_endpoint = city_data["forecast"]

    return forecast_endpoint

def cityData(cordinates):
    city_cords = cordinates
    url = f"https://api.weather.gov/points/{city_cords}"

    city_station_data = requests.get(url, headers=headers)
    city_data = city_station_data.json()

    city = city_data["relativeLocation"]["city"]
    state = city_data["relativeLocation"]["state"]

    return f"{city}, {state}"


def getForecast(endpoint, location):
    city_weather = requests.get(endpoint, headers=headers)
    city_forecast = city_weather.json()

    short_forecast = city_forecast["periods"][0]["shortForecast"]

    return f"{location}: {short_forecast}"

def main():
    cordinates = getCords()
    endpoint = getEndpoint(cordinates)
    city = cityData(cordinates)
    forecast = getForecast(endpoint, city)
    print(forecast)

if __name__ == "__main__":
    main()
