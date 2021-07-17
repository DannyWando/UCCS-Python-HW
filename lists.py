'''
Homework 2, Exercise 3
Daniel Wandeler

This program is a demonstration of the usage and capabilities of lists in Python.
'''

#Part 11 Function Definition
def strList(inputList):
    length = len(inputList)
    output = ''
    for x in range(length-1):
        output += inputList[x] + ', '
    output += 'and ' + inputList[-1]
    print(output)


if __name__ == '__main__':
    #Part 1
    essentials = ['Wallet', 'Phone', 'Keys']
    print(essentials[:])

    #Part 2
    essentials.sort()
    print(essentials[:])

    #Part 3
    print(essentials[0])

    #Part 4
    print(essentials[1:])

    #Part 5
    print(essentials[-1])

    #Part 6
    print(essentials.index('Keys'))

    #Part 7
    essentials.append('Tablet')
    print(essentials[:])

    #Part 8
    essentials.insert(1, 'Mask')
    print(essentials[:])

    #Part 9
    essentials.remove('Phone')
    print(essentials[:])

    #Part 10
    essentials.reverse()
    print(essentials[:])

    #Part 11
    strList(essentials)
    