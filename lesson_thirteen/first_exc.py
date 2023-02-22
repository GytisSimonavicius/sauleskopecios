from typing import Union
from operations import operations

try:
    first_num = int(input('Enter first number: '))
    second_num = int(input('Enter second number: '))
    operation = input('Enter operation sign (+,-,/,*): ')

    final_num = operations[operation](first_num, second_num)
    
    print(f'{first_num} {operation} {second_num} = {final_num}')

except ValueError as ve:
    print(f"Error: {ve}")
except ZeroDivisionError:
    print("Error: division by zero")
except Exception as e:
    print(f"Error: {e}")
