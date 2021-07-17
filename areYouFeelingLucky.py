"""
Homework 7, Exercise 3
Daniel Wandeler

This program acts as a "Are you feeling lucky?" button from Google. It accepts command line arguments as search
terms for Google. The program fetches the search results page from Google and opens it to inspect.
"""
import sys
import webbrowser

googleSearch = 'http://www.google.com/search?q='


def feelingLucky():
    searchTerms = ''
    for i in range(1, len(sys.argv)):
        searchTerms += sys.argv[i] + '+'
    url = googleSearch + searchTerms
    webbrowser.open(url)


feelingLucky()
