'''
Homework 5, Exercise 3
Daniel Wandeler

This program defines a generator that generates the same sequence of values as the range() function without creating
a list object to save memory.
'''


def genrange(stop, start=0, step=1):
    # Set the default start at 0, step at 1
    # Yield every integer from start to step, counting by step
    count = start
    upperLimit = stop
    while count < upperLimit:
        yield count
        count += step


# Code that gets run for tests
print(type(genrange(10)))
print("\n1. genrange(stop)")
for a in genrange(10):
    print(a)

print("\n2. genrange(stop, start)")
for b in genrange(10, 4):
    print(b)

print("\n3. genrange(stop, start, step)")
for c in genrange(10, 4, 2):
    print(c)
