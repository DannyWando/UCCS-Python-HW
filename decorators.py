"""
Homework 6, Exercise 1
Daniel Wandeler

This program is an example of decorators in Python. This decorator is designed to take in an integer argument
for how long to sleep before calling the decorated function.
"""
import functools, time


def slowDown(_func=None, *, sleepTime=1):
    def secondWrapper(func):
        """Sleep 1 second before calling the function"""
        @functools.wraps(func)
        def wrapperSlowDown(*args, **kwargs):
            time.sleep(sleepTime)
            return func(*args, **kwargs)
        return wrapperSlowDown

    if _func is None:
        return secondWrapper
    else:
        return secondWrapper(_func)


@slowDown(sleepTime=3)
def countdown(fromNumber):
    if fromNumber < 1:
        print("Liftoff!")
    else:
        print(fromNumber)
        countdown(fromNumber - 1)


countdown(5)
