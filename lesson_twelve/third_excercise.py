# Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication. Handle all possible errors that may occur.
fromt typing import Union
try:
    first_num = int(input('Enter first number: '))
    second_num = int(input('Enter second number: '))
    operation = input('Enter operation sign (+,-,/,*): ')

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

    if operation not in operations:
        raise ValueError("Invalid operation")

    final_num = operations[operation](first_num, second_num)

    print(f'{first_num} {operation} {second_num} = {final_num}')
except ValueError as ve:
    print(f"Error: {ve}")
except ZeroDivisionError:
    print("Error: division by zero")
except Exception as e:
    print(f"Error: {e}")
