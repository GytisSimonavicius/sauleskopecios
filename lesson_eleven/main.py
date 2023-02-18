# multiplication = lambda x, y: x * y
# print(multiplication(2, 3))

# from typing import Callable

# def get_function(number: int) -> Callable[[int], int]:
#     if number > 1:
#         return lambda: 'Hello'
#     else:
#         return lambda: 'World'
    
# my_function = get_function(2)
# print(my_function())


# def my_funct(n):
#     return lambda a: a * n

# my_doubler = my_funct(2)

# print(my_doubler(3))

from typing import List

list_one = [1, 2, 3, 4, 5]
list_two = [5, 4, 3, 2, 1]

def merge_two_lists(list_one: List, list_two: List) -> List:
    list_sum = [sum(items) for items in zip(list_one, list_two)]
    if len(set(list_sum)) == 1:
        print(True)
    else:
        print(False)
    return list_sum
print(merge_two_lists(list_one, list_two))

