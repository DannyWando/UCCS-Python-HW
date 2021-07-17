'''
Homework 4, Exercise 2
Daniel Wandeler

This program shows 3 Python classes and how to to use class methods to perform calculations.
'''
import math


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def diagonal(self):
        return math.sqrt((self.length ** 2) + (self.width ** 2))

    def perimeter(self):
        return (2 * self.length) + (2 * self.width)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415 * (self.radius ** 2)

    def diagonal(self):
        return self.radius * 2

    def perimeter(self):
        return 3.1415 * 2 * self.radius


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

r1 = Rectangle(20, 10)  # New rectangle with length-20 and width-10
c1 = Circle(r1.diagonal() / 2)  # New circle with radius equal to half of r1's diagonal
finalPerimeter = c1.perimeter()  # Finds perimeter of the new circle
print('The perimeter of the circle specified in the Exercise 2 prompt is %.2f' % finalPerimeter)
