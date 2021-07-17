"""
Homework 7, Exercise 1
Daniel Wandeler

This program uses regular expressions and file IO to change American-style dates to Asian-style dates. It travels
through all files in a directory and makes this adjustment without changing anything else about the file.

This program uses the current working directory as the starting file path of checking for the prompt.
"""
import re
import os
import shutil

path = os.getcwd()
reAmDate = re.compile(r'\d\d-\d\d-\d\d\d\d')
#reAsDate = re.compile(r'\d\d\d\d-\d\d-\d\d')


def amDateChanger():
    for filename in os.listdir(path): #all files in cwd
        if re.search(reAmDate, filename): #if file has an American date
            # Get new string for Asian style date
            replace = reAmDate.search(filename).group(0).split('-')
            newDate = (replace[2] + '-' + replace[0] + '-' + replace[1])

            # Replace to get new string with file path with an updated filename
            newFilename = re.sub(reAmDate, newDate, filename)

            #Officially change the name
            shutil.move(filename, newFilename)


# To go back from Asian style dates to American dates
'''
def asDateChanger():
    for filename in os.listdir(path):
        if re.search(reAsDate, filename):
            replace = reAsDate.search(filename).group(0).split('-')
            newDate = (replace[1] + '-' + replace[2] + '-' + replace[0])
            newFilename = re.sub(reAsDate, newDate, filename)
            print(newFilename)
            shutil.move(filename, newFilename)
'''

amDateChanger()
#asDateChanger()

