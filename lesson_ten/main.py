# a = 5
# b = 7

# def add_number(number1, number2):
#     # sum = number1 + number2
#     return number1 + number2


# c = add_number(10, 15)

# print(c)
#-------------------------

# def print_smth():
#     return 'hello world'


# a = print_smth()

# print(a)
#---------------------------
# my_lst = [1, 2, 3, 4, 5, 6, 7]
# my_lst.append(4)

# print(my_lst)

# import random

# def get_random_number(first_num, last_num):
#     return random.randint(first_num, last_num)   

# a = get_random_number(2,4)

# print(a)
#------------------------------------------------------------------


# ----------------------------------

# def add_two_numbers(number1: int, number2: int) -> int:
#     return number1 + number2

# first_num = input('Enter first number: ')
# second_num = input('Enter second number: ')

# print(add_two_numbers(first_num, second_num))

# # --------
# from typing import List, Tuple, Dict, Union, Optional

# Dicttype_annotation_tuple: Tuple[str] = ('a', 'b', 'c')
# type_annotation_list: List[str] = ['a', 'b', 'c']
# type_annotation_dict: Dict[str, int] = {'a': 1, 'b': 2} 

# def get_random_object() -> Union[int, str, List[str]]:
#     number = random.randint(1, 3)
#     if number == 0:
#         return 0
#     elif number == 1:
#         return 'str'
#     else:
#         return['1', '2', '3']

# def another_function(a: int) -> int:
#     if a > 10:
#         return a
#     else:
#         return None

# Create at least 5 different functions by your own and test it.

# my_list = [1, 2, 3, 4, 5, 6]
# def find_even_numbers():
#     for number in my_list:
#         if number % 2 == 0:
#            print(f'{number} is even')
#         else:
#             print(f'{number} is odd')

# find_even_numbers()


# Create a function that adds a string ending to each member in a list.

# my_lst = ['Tom', 'Jerry', 'Lily', 'Steve', 'Mary']

# def add_string_to_list():
#     for i in range(len(my_lst)):
#         my_lst[i] += '!'
#     return my_lst
# print(add_string_to_list())

# #### or:
# def add_smth_to_list():
#     return [my_lst[i] + '?' for i in range(len(my_lst))]

# print(add_smth_to_list())    

#Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication.

# first_num = int(input('Enter first number: '))
# second_num = int(input('Enter second number: '))
# operation = input('Enter operation sign (+,-,/,*): ')

# def add_two_numbers(first: int, second: int) -> int:
#     return first + second

# def subtract_two_numbers(first: int, second: int) -> int:
#     return first - second

# def multiply_two_numbers(first: int, second: int) -> int:
#     return first * second

# def divide_two_numbers(first: int, second: int) -> float:
#     return first / second

# operations = {
#     '*': multiply_two_numbers,
#     '/': divide_two_numbers,
#     '+': add_two_numbers,
#     '-': subtract_two_numbers,
# }

# final_num = operations[operation](first_num, second_num)

# print(f'{first_num} + {second_num} = {final_num}')
