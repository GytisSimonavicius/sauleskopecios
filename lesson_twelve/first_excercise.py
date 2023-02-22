from typing import Union
 #1. add numbers
def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    try:
        return a + b
    except TypeError:
        print("Please enter two numbers again. It must be a natural number or floating point numbers.")
    except Exception as e:
        print(f'Error: {e}')

# print(add_numbers(1, 4.2))

#2. personal info
def personal_info(first_name: str, last_name: str, age: int) -> Union[str, int]:
    try:
        return f"{first_name} {last_name} is {age} years old."
    except Exception as e:
        return f'Error: {e}'

# print(personal_info("Mary", 'Williams', age=5))


# #3. Make a list with numbers and power it by 3

def power_list(numbers: list) -> list:
    try:
        return [number ** 3 for number in numbers]
    except Exception as e:
        return f'Error: {e}'

# print(power_list([1, 2, 3, 4, '4']))

# 4. take two numbers and check if it's not divide by zero
def divide(first_num: Union[int, float], second_num: Union[int, float]) -> Union[int, float]:
    try:
        return first_num / second_num
    except ZeroDivisionError:
        return "Error: Division by zero"

# print(divide(2, 0))


# 5. This functions checks if number has a perfect square root
import math

def is_square(number: Union[int, float]) -> bool:
    try:
        return math.sqrt(number) % 1 == 0
    except Exception as e:
        return f'Error: {e}'

# print(is_square(25))