'''
Homework 1
Daniel Wandeler
September 8th, 2020

This is a security program that asks the user basic security questions
in order to reveal a secret message.
'''

from random import randint

if __name__ == '__main__':

    #Example of a boolean value
    programOn = True
    points = 0.00
    while programOn:
        #Example of the print() function
        print('Welcome to the security system of many questions.\nEnter your name: ')
        #username is a string variable
        username = input()
        print('Hello,', username)

        #Asks the user the difference of two random numbers
        num2 = randint(1,200) % 30 #uses modulus operator
        num1 = randint(1,100) % 15
        while programOn:
            print('What is the difference between',num1,'and',num2)
            userInput = input();
            if userInput == str(abs(num1 - num2)): #example of the str() function
                print('Well done!')
                break
            elif userInput == 'secret':
                print('Secret code! Try doing the math this time')
                continue
            else:
                print('Try again')
        #The while loop above contains examples of if, else, elif, break, and continue

        #Asks the user one of three state trivia questions
        for i in range(3):
            if i == 0:
                print('What is the capital of Colorado?')
                if input() == 'Denver':
                    print('Well done! Enter a number:')
                    print('You just received', int(input()) % 10, 'points!')
                else:
                    print('Not quite! The capital of Colorado is Denver.')
            elif i == 1:
                print('What is the capital of Texas?')
                if input() == 'Austin':
                    print('Well done!')
                else:
                    print('Not quite! The capital of Texas is Austin.')
            elif i == 2:
                print('What is the capital of Utah?')
                if input() == 'Salt Lake City':
                    print('Well done!')
                else:
                    print('Not quite! The capital of Utah is Salt Lake City.')

        #Gives the user fake points and shows an example of float() and len()
        print('How many points would you like? Enter a number only:')
        points += float(input())
        print('You just earned', points+1, 'points!')
        print('What is your favorite word?')
        print('That word is', len(input()), 'letters long.')

        #Asks the user different math practice problems
        while programOn:
            print('What is the sum of 23 and 5?')
            if input() == '28':
                print('Well done!')
                break
            else:
                print('Try again')
        while programOn:
            print('What is 4 times 4?')
            if input() == '16':
                print('Well done!')
                break
            else:
                print('Try again')

        #Prints the secret message
        print("The secret message is that this program is finished running!")
        print("I never said the secret was going to be good! Bye!")

        #End the while loop program
        if programOn:
            break