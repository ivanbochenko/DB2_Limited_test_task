# Write a function that takes list of tuples (e.g. handle_list_of_tuples(list)) and sort it based on the next rules:
# name / age / height / weight
# Example:
# list = [
#     ("Tom", "19", "167", "54"),
#     ("Jony", "24", "180", "69"),
#     ("Json", "21", "185", "75")
#     ("John", "27", "190", "87"),
#     ("Jony", "24", "191", "98"),
#     ]
# Result:
# [
#     ("John", "27", "190", "87"),
#     ("Jony", "24", "191", "98"),
#     ("Jony", "24", "180", "69"),
#     ("Json", "21", "185", "75"),
#     ("Tom", "19", "167", "54"),
# ]
from operator import itemgetter


def handle_list_of_tuples(list):
    sorted_list = sorted(list, key=itemgetter(0))
    for col in range(len(list[0])):
        for row in range(len(list)):
            if sorted_list[row][col] == sorted_list[row - 1][col]:
                sorted_list[row - 1:row +
                            1] = sorted(sorted_list[row - 1:row + 1], key=itemgetter(col + 1), reverse=True)

    return sorted_list


list = [
    ("Tom", "19", "167", "54"),
    ("Jony", "24", "180", "69"),
    ("Json", "21", "185", "75"),
    ("John", "27", "190", "87"),
    ("Jony", "24", "191", "98"),
]


print(handle_list_of_tuples(list))
