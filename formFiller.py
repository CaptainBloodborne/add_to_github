#! /usr/bin/python3

# formFiller.py - Automatically fills in the form.

import pyautogui
import time

form_data = [
    {
        'name': 'Alice',
        'fear': 'eavesdroppers',
        'source': 'wand',
        'robocop': 4,
        'comments': 'Tell Bob I said hi.'
    },
    {
        'name': 'Bob', 'fear': 'bees',
        'source': 'amulet',
        'robocop': 4,
        'comments': 'n/a'
    },
    {''
     'name': 'Carol',
     'fear': 'puppets', 'source': 'crystal ball',
     'robocop': 1,
     'comments': 'Please take the puppets out of the break room.'
     },
    {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
     'robocop': 5,
     'comments': 'Protect the innocent. Serve the publictrust. Uphold the law.'
     },
]

pyautogui.PAUSE = 0.5

print('Ensure that the browser windows is active and the form is loaded!')

for person in form_data:
    # Give the user a chance to kill the script
    print('>>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<<')
    time.sleep(5)

    print(f"Entering {person['name']} info...")
    pyautogui.write(['\t', '\t'], 0.5)

    # Fill out the name Field
    pyautogui.write(person['name'] + '\t')
    
    # Fill out the Greatest Fear(s) field
    pyautogui.write(person['fear'] + '\t')

    # Fill out the Source of Wizard Powers Field.
    if person['source'] == 'wand':
        pyautogui.write(['down', '\n', '\t'], 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', '\n', '\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', '\n', '\t'], 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', '\n', '\t'], 0.5)

    if person['robocop'] == 1:
        pyautogui.write([' ', '\t', '\t'], 0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t', '\t'], 0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t', '\t'], 0.5)
        
    # Fill out the Additional comments field.
    pyautogui.write(person['comments'] + '\t')

    # Click the submit button by pressing Enter
    pyautogui.write('\n')
    print('Submitted form')
    time.sleep(5)

    # Click the Submit another response link
    # pyautogui.click(submit_another_link[0], submit_another_link[1])
    pyautogui.write(['\t', '\n'])
    time.sleep(5)
