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


def e_sort(list):
    return list[0][0]


# def handle_list_of_tuples(list):
#     sorted_list = []
#     for i in list:


list = [
    ("Tom", "19", "167", "54"),
    ("Jony", "24", "180", "69"),
    ("Json", "21", "185", "75")
    ("John", "27", "190", "87"),
    ("Jony", "24", "191", "98"),
]

s_list = sorted(list, key=e_sort)

print(s_list)
# print(handle_list_of_tuples(list))
