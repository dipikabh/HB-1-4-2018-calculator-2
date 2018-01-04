"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

import arithmetic


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
    tokens = user_input.split(" ")
    num1 = float(tokens[1])
    num2 = float(tokens[2])

    if tokens[0] == "q":
        break

    elif tokens[0] == "+":
        print arithmetic.add(num1, num2)
