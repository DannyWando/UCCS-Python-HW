"""
Homework 3, Exercise 2
Daniel Wandeler

This program counts the number of occurrences of each character in a string. It then
creates a dictionary containing the previously mentioned data and prints it.
"""

import pprint

#inputTest = 'The quick brown fox jumps over the lazy dog.'

if __name__ == '__main__':
    string = {}
    inputString = str(input('Please enter a string: '))
    for char in inputString:
        if char in string:
            string[char] += 1
        else:
            string[char] = 1
    pprint.pprint(string)
    