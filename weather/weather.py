# -*- coding: utf-8 -*-
#!/usr/bin/python
import pyowm # pip install pyowm

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
        if self.unit is 'C':
            celsius = pyowm.utils.temputils.kelvin_to_celsius(temp_in_kelvin['temp'])
            if status == 'Clouds':
                return ' {}, {}°C'.format(status, celsius)
            elif status == 'Clear':
                return ' {}, {}°C'.format(status, celsius)
            elif (status == 'Rain') or (status == 'Thunderstorm') or (status == 'Drizzle'):
                return ' {}, {}°C'.format(status, celsius)
        elif self.unit is "F":
            fahrenheit = pyowm.utils.temputils.kelvin_to_fahrenheit(temp_in_kelvin['temp'])
            if status == 'Clouds':
                return ' {}, {}°F'.format(status, fahrenheit)
            elif status == 'Clear':
                return ' {}, {}°F'.format(status, fahrenheit)
            elif status == 'Rains' or status is 'Thunderstorm':
                return ' {}, {}°F'.format(status, fahrenheit)

if __name__ == '__main__':
    reporter = WeatherGetter('YOUR CITY, YOUR 2-LETTER COUNTRY CODE','YOUR UNIT HERE')

    weather = reporter.get_weather_of_city()

    status = reporter.get_status_of_city(weather)
    temp = reporter.get_temp_of_city(weather)

    print (reporter.output_the_weather(temp, status))
