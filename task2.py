# Write a function that takes sentense as a parameter (e.g. handle_string(value))
# and count number of letters and digits.
# Example:
# value = "Hello world! 123!"
# Result:
# Letters -  10
# Digits -  3


def handle_string(value):
    letters = 0
    digits = 0
    for char in value:
        if char.isalpha() is True:
            letters += 1
        elif char.isdigit() is True:
            digits += 1
    print('String consists of {0} letters and {1} digits'.format(letters, digits))


handle_string("Hello world! 123!")
