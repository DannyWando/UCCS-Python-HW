'''
Homework 2, Exercise 2
Daniel Wandeler

This program is a demonstration of the collatz sequence and input validation.
'''

'''
This function uses a recursive loop to show the collatz sequence.
If the number is even, it is halved and recursively called again.
If the number is odd, it is multiplied by 3, added 1, and called again.
The process will stay in the recursive loop until the number equals 1.
'''

def collatz(number):
    if number == 1:
        print(number)
    elif number % 2 == 0:
        print(number)
        collatz(number//2)
    else:
        print(number)
        collatz(3*number+1)


if __name__ == '__main__':
    while True:
        try:
            inputNumber = int(input('Please enter an integer below: '))
            break
        except ValueError:
            print("That's not a valid input. Enter an integer: ")
    collatz(inputNumber)
