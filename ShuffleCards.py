'''
Daniel Wandeler
Card Shuffler for Games using a standard 52-card deck

This function creates a list representing a randomly shuffled 52 card deck to be used for table games
such as poker, blackjack, spades, etc...
'''

import random
import copy

# Define the card types and values
FACE = {
    "ACE": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "JACK": 10,
    "QUEEN": 10,
    "KING": 10,
}

TYPE = ["CLUBS", "SPADES", "HEARTS", "DIAMONDS"]


# used for the dictionary definition of the cards
def get_key(dict1):
    return list(dict1.keys())


def get_values(dict1):
    return list(dict1.values())


# shuffles the deck to allow dictionary values
def shuffled_deck(n):
    shuffled_cards = {}
    created_deck = {}
    face = get_key(FACE)
    value = get_values(FACE)

    for i in range(0, (len(FACE))):  # amount of face cards
        for j in TYPE:
            created_deck[face[i] + " of " + j] = value[i]

    list_multiplier = list(created_deck.items()) * n
    shuffler = copy.deepcopy(list_multiplier)
    print(shuffler)
    random.shuffle(shuffler)
    print('\n\n\n', shuffler, len(shuffler))
    shuffled_cards = dict(shuffler)

    print('\n\n\n', shuffled_cards)
    return shuffled_cards


x = shuffled_deck(5)
print('\n\n\n',x, len(x))
