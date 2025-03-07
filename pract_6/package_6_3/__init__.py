import math

def calculate_area(shape):
    if shape==1: # circle
        radius = int(input("Enter radius: "))
        return circle(radius)
    elif shape==2: # rectangele
        length=int(input("Enter length: "))
        width=int(input("Enter width: "))
        return rectangle(length, width)
    elif shape==3: # triangle
        base=int(input("Enter base: "))
        height=int(input("Enter height: "))
        return triangle(base, height)

def circle(radius):
    return radius * 2 * math.pi

def rectangle(length, width):
    return length * width

def triangle(base, height):
    return base * height * 0.5

def prime(number):
    if number == 1:
        return True
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
