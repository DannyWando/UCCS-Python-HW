"""
Homework 6, Exercise 2
Daniel Wandeler

This program is an example using decorators to get better performance calculating a Fibonacci sequence.
The cache decorator will save the calculations in a dictionary, then the program will apply the countCalls decorator
from lecture.

Conclusion:
Using the countCalls decorator on the Fibonacci function showed the amount of calls is insanely high. I tested using
fibonacci(25) and ended up with 242785 function calls before it finished. With the cache decorator, I used fibonacci(25)
and ended up with 49 calls of the function. I did another test with fibonacci(250) and without cache, 11658861 before
quitting the function manually since no end was in sight, and with cache, 499. The performance optimization is major.
"""
import functools


def cache(func):
    func.dict = {}
    @functools.wraps(func)
    def wrapperDecorator(*args, **kwargs):
        if args in func.dict:
            return func.dict[args]
        else:
            value = func(*args, **kwargs)
            func.dict[args] = value
            return value
    return wrapperDecorator


def countCalls(func):
    @functools.wraps(func)
    def wrapperCountCalls(*args, **kwargs):
        wrapperCountCalls.numCalls += 1
        print("Call {} of {}".format(wrapperCountCalls.numCalls, func.__name__))
        return func(*args, **kwargs)
    wrapperCountCalls.numCalls = 0
    return wrapperCountCalls


@countCalls
@cache
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


fibonacci(250)
