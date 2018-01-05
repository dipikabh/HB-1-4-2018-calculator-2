"""A prefix-notation calculator.

Using the py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# # No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token

while True:
    user_input = raw_input("> ")

    if user_input == "q":
        break

    tokens = user_input.split(" ")
    # print tokens
    # print len(tokens)

    if len(tokens) == 2:
        num1 = float(tokens[1])

        if tokens[0] == "square":
            print square(num1)

        elif tokens[0] == "cube":
            print cube(num1)

        else:
            print "Please type square or cube, followed by one integer."

    elif len(tokens) == 3:
        num1 = float(tokens[1])
        num2 = float(tokens[2])

        if tokens[0] == "+":
            print add(num1, num2)

        elif tokens[0] == "-":
            print subtract(num1, num2)

        elif tokens[0] == "*":
            print multiply(num1, num2)

        elif tokens[0] == "/":
            print divide(num1, num2)

        elif tokens[0] == "pow":
            print power(num1, num2)

        elif tokens[0] == "%" or tokens[0] == "mod":
            print mod(num1, num2)

        else:
            print "Please type a valid operator, followed by two integers."

    else:
        print """
        Sorry, that's not valid input!
        (Please start with an operator, followed by up to 2 intergers.)
            """
