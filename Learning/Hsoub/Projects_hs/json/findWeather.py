import requests, json, math
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template('weather.html')

@app.route("/api/weather")
def weatherApi():
    api_key = 'c516e3a0289cc01f6a2383b5d14eda80'

    baseUrl = 'https://api.openweathermap.org/data/2.5/weather?'

    cityName = request.args.get('city')
    if not cityName: return "No City Name is given"


    completeUrl = baseUrl + 'q=' + cityName + '&units=metric' + '&appid=' + api_key

    response = requests.get(completeUrl)

    x = json.loads(response.text)

    if x['cod'] != '404':

        y = x['main']

        temp = y['temp']
        pressure = y['pressure']
        humidity = y['humidity']
        weather = x['weather']

        weatherDesc = weather[0]['description']

        api = json.dumps({
            "temp": temp,
            "pressure": pressure,
            "humidity": humidity,
            'weather': weather,
            'weatherDesc': weatherDesc
        })

        print("Temp (metric) = " + str(temp) + '\n pressure (metric) = ' + str(
            pressure) + '\n humidity (metric) = ' + str(humidity) + '\n description = ' + str(weatherDesc))


    else:
        return
    return api

