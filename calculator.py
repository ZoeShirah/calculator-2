"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic2 import *


def validate(lst, pos):

    try:
        num = int(lst[pos])
    except (IndexError, ValueError):
        print "I don't understand"
        num = None
    return num

while True:

    equation = raw_input("> ").split()

    if equation[0] == "q":
        break

    first = validate(equation, 1)
    if not first:
        continue

    if equation[0] == "square":
        print square(first)
    elif equation[0] == "cube":
        print cube(first)
    else:

        second = validate(equation, 2)
        if not second:
            continue

        if equation[0] == "+":
            print add(first, second)
        elif equation[0] == "-":
            print subtract(first, second)
        elif equation[0] == "*":
            print multiply(first, second)
        elif equation[0] == "/":
            print divide(first, second)
        elif equation[0] == "pow":
            print power(first, second)
        elif equation[0] == "mod":
            print mod(first, second)
        else:
            print "I don't understand"
