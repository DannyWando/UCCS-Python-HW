'''
Homework 4, Exercise 3
Daniel Wandeler

This program serves as an email and phone number. It takes in a large chunk of text and returns phone numbers
and email addresses and pastes them to the clipboard.
'''
import pyperclip, re


def findContacts(clipboard):
    # Regexs defined
    phoneNumRegex = re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d)')
    emailRegex = re.compile(r'\S+@\S+')

    # Find phone number and email matches
    phoneContacts = phoneNumRegex.findall(str(clipboard))
    emailContacts = emailRegex.findall(str(clipboard))
    contacts = ''

    # Read all the matches into a single string
    for i in range(len(phoneContacts)):
        contacts += str(phoneContacts[i]) + '\n'
    for j in range(len(emailContacts)):
        contacts += str(emailContacts[j]) + '\n'

    return contacts

contactList = findContacts(pyperclip.paste())
pyperclip.copy(contactList)
