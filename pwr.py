#! /usr/bin/python3.  
# pwr.py - Application for unsecured storage of passwords
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to the keyword
#        py.exe mcb.pyw <keyword> - Loads keyword to the clipboard
#        py.exe mcb.pyw list - Loads all keywords to clipboard
#        py.exe mcb.pyw <account> - loads password to clipboard

import shelve
import pyperclip
import sys

PASSWORDS = {}

pwr_shelf = shelve.open('pwr')
pwr_shelf['passwords'] = PASSWORDS

# TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    pwr_shelf[sys.argv[2]] = pyperclip.paste()
elif sys.argv[1].lower() == 'delete' and len(sys.argv) == 3:
    del pwr_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # TODO: List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy((str(list(pwr_shelf.keys()))))
    elif sys.argv[1] in pwr_shelf:
        pyperclip.copy(pwr_shelf[sys.argv[1]])

    elif sys.argv[1] in pwr_shelf['passwords']:
        pyperclip.copy(pwr_shelf['passwords'][sys.argv[1]])
        print('Password is', sys.argv[1], 'copied to clipboard')
    elif sys.argv[1].lower() == 'delete_all':
        pwr_shelf.clear()
    else:
        print('No such argument or account exists')
        print("""Usage: 
       py.exe pwr.py save <keyword> - Saves clipboard to the keyword
       py.exe pwr.py <keyword> - Loads keyword to the clipboard
       py.exe pwr.py list - Loads all keywords to clipboard
       py.exe pwr.py <account> - loads password to clipboard 
       py.exe pwr.py delete <keyword> - remove keyword from shelf
       py.exe pwr.py delete_all  - remove all keywords from shelf
       """)


pwr_shelf.close()



