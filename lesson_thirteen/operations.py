from typing import Union
def add_two_numbers(first: int, second: int) -> int:
    return first + second

def subtract_two_numbers(first: int, second: int) -> int:
    return first - second

def multiply_two_numbers(first: int, second: int) -> int:
    return first * second

def divide_two_numbers(first: int, second: int) -> Union[float, int]:
    return first / second


operations = {
    '*': multiply_two_numbers,
    '/': divide_two_numbers,
    '+': add_two_numbers,
    '-': subtract_two_numbers,
}