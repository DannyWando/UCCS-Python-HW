'''
Text File to DFA Converter
Daniel Wandeler
CS 4700 NFA Assignment

This program reads in a file with a specific format and creates a DFA with it. Then,
the program executes the defined DFA on user-entered input strings.

DFA that accepts the language:
    {w over {a,b}* | w has at least 2 consecutive a's}
'''
import re



class DFA:
    # Initializer
    def __init__(self, alphabet, numStates, transitions, accept):
        self.alphabet = alphabet
        self.numStates = numStates
        self.accept = accept
        self.transitions = transitions

    # Test the given input string to see if it's accepted by the DFA or not
    def testDFA(self, inputString):
        currentState = 0
        finalState = self.accept
        for j in range(len(inputString)):
            if inputString[j] in self.alphabet:
                moveIndex = int(self.alphabet.find(inputString[j]))
                currentState = int(self.transitions[currentState][moveIndex])
            else:
                print('The string', inputString, 'has some characters not found in the alphabet.')
                return 0
        if str(currentState) in finalState:
            print('This string', inputString, 'is ACCEPTED by the DFA.')
        else:
            print('This string', inputString, 'is REJECTED by the DFA.')


def createDFA(dfaFile):
    parsedString = dfaFile.split('\n')
    untilWhitespaceRegex = re.compile(r'[^\s]+')

    # transitionRegex gets all characters up until a semicolon character.
    # This regex will not work if the file isn't formatted with a semicolon before the new line.
    # Included below is a comment that was directly copy/pasted from the DFA_Input file used in testing.
    transitionRegex = re.compile(r'^.*;')

    scope = str(untilWhitespaceRegex.search(parsedString[0])[0])

    numStates = int(untilWhitespaceRegex.search(parsedString[1])[0])

    transitionRules = []
    for x in range(numStates):
        tmp = x
        tmpString = str(transitionRegex.search(parsedString[tmp+2])[0]).replace(' ;', '')
        ruleList = tmpString.split(' ')
        transitionRules.append(ruleList)

    accept = str(transitionRegex.search(parsedString[numStates+2])[0]).replace(' ;', '')

    return DFA(scope, numStates, transitionRules, accept)


with open(r'C:\Users\Skinny P\Downloads\DFA1.txt') as inputFile:
    fileString = inputFile.read().replace('\t', ' ')
    # Removes tabs and replaces for space characters since the parsing splits on spaces

testStrings = ['abba', 'bababb', 'abaaba', 'aaba', 'bbabaa']
newDFA = createDFA(fileString)
for i in range(len(testStrings)):
    newDFA.testDFA(testStrings[i])
print('\nProgram completed running.')
inputFile.close()
