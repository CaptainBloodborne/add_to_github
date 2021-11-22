#! usr/bin/python3

# linkVerify.py - attempts to download every linked page on the page
# and flags any pages that have a 404 "Not found" status code

import sys
import bs4
import requests
import os

os.makedirs('/home/artem/Documents/web_pages', exist_ok=True)

url = sys.argv[1]  # starting url taken from command line

# Download the page

print(f'Downloading page {url}')
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Find the url of the all pages.

page_elems = soup.select('a[href]')

# Download and store every page in html file
os.chdir('/home/artem/Documents/web_pages')
for page in page_elems:
    print(f"Downloading page {page.attrs['href']}")
    try:
        res = requests.get(page.attrs['href'])
        res.raise_for_status()
        if res.status_code == 404:  # check the status
            print(f"Page {page.attrs['href']} not found")
            continue
        # Save page as html file
        web_page_file = open(os.path.basename(page.attrs['href']) + '.html', 'wb')
        for chunk in res.iter_content(1000000):
            web_page_file.write(chunk)
        web_page_file.close()
    except Exception as err:
        print(err)
        print(f"Unnable to download {page.attrs['href']}")
