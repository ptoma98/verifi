import argparse
import requests
import json

DEFAULT_CITY = "Los Angeles"
API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_current_weather(city, api_key):
    payload = {'q': city, 'appid': api_key, 'units': 'imperial'}
    response = requests.get(API_URL, params=payload)
    return json.loads(response.content)


def report_weather(city, weather):
    desc = weather['weather'][0]['description']
    temp = weather['main']['temp']
    low = weather['main']['temp_min']
    high = weather['main']['temp_max']
    print(f"Current {city} Weather: {desc}, current temperature is {temp} degrees fahrenheit, low of {low}, with a high of {high}.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--city", required=False, help="City to get current weather", default=DEFAULT_CITY)
    parser.add_argument("-k", "--key", required=True, help="OpenWeather API KEY")

    args = parser.parse_args()
    city = args.city
    key = args.key

    weather = get_current_weather(city, key)

    report_weather(city, weather)


if __name__ == "__main__":
    main()


