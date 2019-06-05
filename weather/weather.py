# -*- coding: utf-8 -*-
#!/usr/bin/python
import pyowm

class WeatherGetter(object):
    # How to enter the argument city:
    #   (your city),(your two letter country code)
    #   for example, the argument for London would be:
    #   'London,gb'

    # How to enter the argument unit:
    #   Enter a string, 'C' or 'F' for Celsius unit or Fahrenheit unit respectively.
    def __init__(self, city, unit, api_key):
        self.city = city
        self.unit = unit
        self.api_key = api_key # get api key from OWM after signing up

    def get_weather_of_city(self):
        owm = pyowm.OWM(self.api_key)
        weather_in_city = owm.weather_at_place(self.city)
        weather = weather_in_city.get_weather() # returns a Weather object, with
        # the temperature, status, etc.
        return weather

    def get_temp_of_city(self, weather):
        temp_in_kelvin = weather.get_temperature() # Returns a dict
        return temp_in_kelvin

    def get_status_of_city(self, weather):
        status = weather.get_status() # for eg. sunny, clouds, etc.
        return status
    def output_the_weather(self, temp_in_kelvin, status):
        psbl = {'Clouds':' ',
                'Haze': ' ' ,
                'Clear': ' ',
                'Rain': ' ',
                'Thunderstorm': ' ',
                'Drizzle': ' ',
                'Dust': ' '}

        icon = psbl.get(status)

        if self.unit is 'C':
            tmp = pyowm.utils.temputils.kelvin_to_celsius(temp_in_kelvin['temp'])

        elif self.unit is "F":
            tmp = pyowm.utils.temputils.kelvin_to_fahrenheit(temp_in_kelvin['temp'])
        
        return "{}{}, {}°{}".format(icon, status, tmp, self.unit)

if __name__ == '__main__':
    reporter = WeatherGetter('city, 2-letter country code','your unit here','api-key-here')

    weather = reporter.get_weather_of_city()

    status = reporter.get_status_of_city(weather)
    temp = reporter.get_temp_of_city(weather)

    print (reporter.output_the_weather(temp, status))
