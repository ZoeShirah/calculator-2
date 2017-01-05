"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic2 import *


def validate(lst, length):

    if length == 0:
        length = len(lst) + 1
    num_list = []
    for x in range(1, length + 1):
        try:
            num = int(lst[x])
        except (IndexError, ValueError):
            print "I don't understand"
            return []
        num_list.append(num)
    return num_list

while True:

    equation = raw_input("> ").split()

    if equation[0] == "q":
        break

    one = ["square", "cube"]
    two = ["-", "/", "pow", "mod"]
    more = ["+", "*"]
    if equation[0] in one:
        num_list = validate(equation, 1)
        if num_list == []:
            break
        elif equation[0] == "square":
            print square(num_list[0])
        elif equation[0] == "cube":
            print cube(num_list[0])

    elif equation[0] in two:
        num_list = validate(equation, 2)
        if num_list == []:
            break
        elif equation[0] == "-":
            print subtract(num_list[0], num_list[1])
        elif equation[0] == "/":
            print divide(num_list[0], num_list[1])
        elif equation[0] == "pow":
            print power(num_list[0], num_list[1])
        elif equation[0] == "mod":
            print mod(num_list[0], num_list[1])

    elif equation[0] in more:
        num_list = validate(equation, 0)
        if num_list == []:
            break
        elif equation[0] == "+":
            print reduce(add, num_list)
        else:
            print reduce(multiply, num_list)

    else:
        print "I don't understand"
