#! usr/bin/python3

# getForecast.py - Prints the weather for a location from command line.
import json
import sys
import requests
import logging
import pprint

APP_ID = '090ff769136f3710966170675d12296c'

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname) s - %(message)s')
logging.disable(logging.CRITICAL)

# Compute location from commandline arguments.

if len(sys.argv) < 2:
    print('Usage: getForecast.py city_name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])
logging.debug('{} is location'.format(location))

# Download the JSON data from OpenWeatherMap.org's API.

url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&APPID={}'.format(location, APP_ID)
response = requests.get(url)
response.raise_for_status()


# Uncomment to see the raw JSON text
# print(response.text)

# Load JSON data into a Python variable.
weather_data = json.loads(response.text)
pprint.pprint(weather_data)

# Print weather descriptions.

w = weather_data['list']
print('Current weather in {}:'.format(location), '\n')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'], '\n')
print('Tomorrow')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'], '\n')
print('Day after tomorrow')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'], '\n')
