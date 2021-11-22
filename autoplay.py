# autoplay.py - plays 2048 game automatically.

import logging
from random import choice

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname) s - %(message)s')
logging.disable(logging.CRITICAL)


# Open browser controlled by selenium and go to play2048.co
def play_game(browser, adress):
    """
    Opens browsers and enter required website
    :param browser: defines required browser and webdriver to use
    :param adress: defines website
    :return:
    """
    browser.get(adress)
    html_elem = browser.find_element_by_tag_name('html')
    # Start playing loop until game over
    while True:
        choice(
            [
             html_elem.send_keys(Keys.UP),
             html_elem.send_keys(Keys.RIGHT),
             html_elem.send_keys(Keys.DOWN),
             html_elem.send_keys(Keys.LEFT),
            ]
        )
        # Check if game is finished
        retry_elem = browser.find_element_by_class_name('game-message')
        if retry_elem.text == 'Game over!\nTry again':
            new_elem = browser.find_element_by_class_name('retry-button')
            new_elem.click()
            continue


if __name__ == "__main__":
    browser = webdriver.Firefox()
    adress = "https://www.play2048.co"
    play_game(browser, adress)
