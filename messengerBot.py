#! /usr/bin/python3

# messengerBot.py - sends messeges via messengers automatically
# usage 'messengerBot.py contactName "message" 

import subprocess
import pyautogui
import sys
import time
import logging

logging.basicConfig(filename='control_logging.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname) s - %(message)s')
#logging.disable(logging.CRITICAL)

pyautogui.PAUSE = 0.5
message = input('Enter your message here: ') 
name_list = sys.argv[1:]
messenger = subprocess.Popen('/usr/bin/telegram-desktop')
time.sleep(5)

# Add 'for' loop to iterate through names and send message to multiple contacts
for name in name_list:
    logging.debug(f'Message is {message}')
    pyautogui.write(name + '\n', 0.5)
    pyautogui.write(message + '\n', 1.0)
    pyautogui.click('/home/artem/Pictures/search.png')

# TODO: Check if message was sent or not




