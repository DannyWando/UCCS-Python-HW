'''
Homework 5, Exercise 2
Daniel Wandeler

This program uses a generator comprehension expression to find the first n pythagorean triplets. N is a
given integer that is passed as an argument to the function call.
'''

import math

# From lecture slides 8_Iterators_and_generators.pdf
def integers():
    i = 1
    while True:
        yield i
        i += 1


# From lecture slides 8_Iterators_and_generators.pdf
def take(n, seq):
    seq = iter(seq)

    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result

''' 
Started using a generator, but noticed the prompt asked for a generator comprehension expression

def pythTriple():
    for y in integers():
        for x in range(1, y):
            z = math.sqrt(x*x + y*y)
            if z % 1 == 0:
                yield (x, y, int(z))
'''

# Generator comprehension expression
# Wrote the generator first to get an idea, then condensed it down into a single expression
pythagoreanTriple = ((x,y, int(math.sqrt(x*x + y*y))) for y in integers() for x in range(1, y) if math.sqrt(x*x + y*y) % 1 == 0)

print(take(10, pythagoreanTriple))
