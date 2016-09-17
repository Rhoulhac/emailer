import requests

def get_weather_forecast():
    # Connecting to weather API and getting JSON
    url = 'http://api.openweathermap.org/data/2.5/weather?q=DesMoines,ia&units=imperial&appid=6308ac143ccae5ba69aa47a4f334ab1e'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    # Info from JSON
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    forecast = "The forcast for today is " + description + " with a high of "
    forecast += str(int(temp_max)) + " and a low of " + str(int(temp_min))
    return forecast
