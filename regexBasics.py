'''
Homework 4, Exercise 4
Daniel Wandeler

This program uses regular expressions to make sure a password string is strong enough. It takes in a string as
input and checks it for length, certain characters, and digits.
'''
import re

def passwordStrength(password):
    # Regexs defined
    lengthRegex = re.compile(r'^\S{8,}$')
    caseRegex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])')
    digitRegex = re.compile(r'(?=.*\d)')

    if str(lengthRegex.search(password)) == 'None':
        print('length')
        return False
    else:
        if str(caseRegex.search(password)) == 'None':
            print('case')
            return False
        else:
            if str(digitRegex.search(password)) == 'None':
                print('digit')
                return False
            else:
                return True


maybePassword = input('Enter a new password: ')
if passwordStrength(maybePassword):
    print('That is a strong password!')
else:
    print('That password is not strong enough...')