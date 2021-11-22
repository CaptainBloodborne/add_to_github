#! usr/bin/python3

# cmdLineEmailer.py - takes am email adress and string of text on the command line
# then logs into email account and sends an email

from selenium import webdriver
import sys
import logging
import time

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname) s - %(message)s')
#logging.disable(logging.CRITICAL)

if len(sys.argv) < 2:
    print('Usage: cmdLineEmailer.py password email_adress "Message text"')
    sys.exit()
    
browser = webdriver.Firefox()
browser.get('https://www.mail.ru')
login_elem = browser.find_element_by_name('login')
login_elem.send_keys('vrail30')
button_elem = browser.find_element_by_css_selector('.button')
button_elem.click()
pass_elem = browser.find_element_by_name('password')
pass_elem.send_keys(sys.argv[1])
button_elem = browser.find_element_by_css_selector('.second-button')
button_elem.click()
browser.refresh()
time.sleep(1)
compose_elem = browser.find_element_by_css_selector('.compose-button__txt')
compose_elem.click()
time.sleep(2)
contact_elem = browser.find_element_by_xpath("//input[@tabindex='100']")

contact_elem.send_keys(sys.argv[2])
message_elem = browser.find_element_by_xpath("//div[1][@tabindex='505']")
message_elem.send_keys(sys.argv[3])
send_elem = browser.find_element_by_css_selector('''span.button2_base:nth-child(1) 
> span:nth-child(1) > span:nth-child(1)''')
send_elem.click()
