"""
Homework 2, Exercise 4
Daniel Wandeler

This program is a 'Guess the Number' game. The program comes up with a random number between 1 and 20,
and the player has to guess the number within 10 tries. The program will tell you if you are too high,
too low, incorrect, or correct. The game changes by using randomly generated upper and lower bounds, and
it also has an automatic version where the computer plays itself.
"""

import random

def guessTheNumber(lowerB, upperB):
    magicNumber = random.randint(lowerB, upperB)
    winner = False
    numTries = 10
    print('I am thinking of a number between {} and {}. You have 10 tries.'.format(lowerB,upperB))
    for x in range(numTries):
        guess = int(input('Take a guess.\n'))
        if (guess == magicNumber):
            print('Good job! You guessed my number in', x+1 , 'guesses!')
            winner = True
            break
        elif (guess < magicNumber):
            print('Your guess is too low.')
        elif (guess > magicNumber):
            print('Your guess is too high.')
        else:
            continue
    if not winner:
        print('Sorry the number I was thinking of was {}.'.format(magicNumber))


def autoGuessTheNumber(lowerB, upperB):
    magicNumber = random.randint(lowerB, upperB)
    winner = False
    numTries = 10
    print('I am thinking of a number between {} and {}. You have 10 tries.'.format(lowerB,upperB))
    #Guessing game logistics
    for x in range(numTries):
        guess = random.randint(lowerB, upperB)
        print(guess)
        if (guess == magicNumber):
            print('Good job! You guessed my number in', x+1 , 'guesses!')
            winner = True
            break
        elif (guess < magicNumber):
            print('Your guess is too low.')
        elif (guess > magicNumber):
            print('Your guess is too high.')
        else:
            continue
    if not winner:
        print('Sorry the number I was thinking of was {}.'.format(magicNumber))


if __name__ == '__main__':
    #Finds a random upper and lower bound, making sure that the lower bound is actually less than the upper bound
    randLowerB = random.randint(0, 1000)
    randUpperB = random.randint(0, 1000)
    if randLowerB > randUpperB:
        temp = randUpperB
        randUpperB = randLowerB
        randLowerB = temp

    #Part1
    guessTheNumber(1,20)
    #Part 2
    guessTheNumber(randLowerB, randUpperB)
    #Part3
    autoGuessTheNumber(randLowerB, randUpperB)
