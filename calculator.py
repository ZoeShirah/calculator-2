"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:

    equation = raw_input("> ").split()

    if equation[0] == "q":
        break

    try:
        first = int(equation[1])
    except (IndexError, ValueError):
        print "I don't understand"
        continue

    if equation[0] == "square":
        print square(first)
    elif equation[0] == "cube":
        print cube(first)
    else:
        try:
            second = int(equation[2])
        except (IndexError, ValueError):
            print "I don't understand"
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
