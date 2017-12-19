# Write a function that takes as a parameters
# number1(int), number2(int) and number3. (e.g. handle_numbers(number1, number2, number3))
# Function need to return the count of integers that are divisible by number3 in range [number1, number2]
# Example:
# number1 = 1
# number2 = 10
# number3 = 2
# Result:
# 5, because 2, 4, 6, 8, 10 are divisible by 2


def handle_numbers(number1, number2, number3):
    count = 0
    for i in range(number1, number2 + 1):
        if i % number3 == 0:
            count += 1
    return count


print(handle_numbers(1, 10, 2))
print(handle_numbers(4, 20, 5))
