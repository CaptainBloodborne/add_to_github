#! usr/bin/python3

# getForecast.py - Prints the weather for a location from command line.

APP_ID = '090ff769136f3710966170675d12296c'

import json
import sys
import requests
import logging
import smtplib

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname) s - %(message)s')
logging.disable(logging.CRITICAL)

# Compute location from commandline arguments.

if len(sys.argv) < 1:
    print('Usage: randomChore.py email_password')
    sys.exit()

location = 'Nizhniy Novgorod, RU'
password = sys.argv[1]
logging.debug('{} is location'.format(location))

# Download the JSON data from OpenWeatherMap.org's API.

url ='https://api.openweathermap.org/data/2.5/forecast?q={}&APPID={}'.format(location, APP_ID)
response = requests.get(url)
response.raise_for_status()


# Uncomment to see the raw JSON text
#print(response.text)

# Load JSON data into a Python variable.
weather_data = json.loads(response.text)

# Print weather descriptions.

w = weather_data['list']
print('Current weather in {}:'.format(location), '\n')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'], '\n')
print('Tomorrow')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'], '\n')
print('Day after tomorrow')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'], '\n')

# Send reminder so email account
if 'clouds' in w[0]['weather'][0]['description']:
    # Login to email account
    smtp_obj = smtplib.SMTP('smtp.mail.ru', 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login('vrail30@mail.ru', password)
    # Send reminder to email
    body = ('Subject: Umbrella.\nDear me, please don\'t forget to take umbrella today, because it is raining!')
    sendemail_status = smtp_obj.sendmail('vrail30@mail.ru', 'vrail30@gmail.com', body)
    print('Sending reminder to vrail30@gmail.com')
    
    if sendemail_status != {}:
        print(f'There was proble sending email to your adress: {sendemail_status}')
smtp_obj.quit()

# TODO: Send reminder to cellphone

  

