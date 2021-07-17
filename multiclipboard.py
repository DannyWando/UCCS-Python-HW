"""
Homework 6, Exercise 3
Daniel Wandeler

This program is a multi-clipboard implementation in Python. The program will save each piece of clipboard copied text
under a keyword. Then, when the program is run with a keyword argument, the current contents of the clipboard will
update to match what is associated with the keyword. The user can also use argument 'list' to see all saved text, and
'save' to take the current clipboard contents and save them to the multi-clipboard program.
"""

import sys
import pyperclip
import shelve


shelfFile = shelve.open('newMultiClip')
def multiclipboard(command, identifier):
    if command == 'save':
        shelfFile[identifier] = str(pyperclip.paste())
        return 0
    elif command == 'list':
        print(list(shelfFile.keys()))
        return 0
    else:
        pyperclip.copy(shelfFile[identifier])
        return 0

if (len(sys.argv)) == 2:
    if str(sys.argv[1]) == 'list':
        multiclipboard(str(sys.argv[1]), '')
    else:
        multiclipboard('', str(sys.argv[1]))
elif (len(sys.argv)) == 3:
    multiclipboard(str(sys.argv[1]), str(sys.argv[2]))


shelfFile.close()
