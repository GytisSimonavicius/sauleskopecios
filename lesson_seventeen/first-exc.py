from typing import Union

class Calculator:
    description: str = "Welcome to the calculator!"
    
    def __init__(self):
        pass

    @classmethod
    def get_numbers(cls):
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        operator = input("Enter operator (*,/,+,-): ")
        return cls._calculate(first_number, operator, second_number)

    @staticmethod
    def _calculate(first_number: Union[int, float], operator: str, second_number: Union[int, float]):
        calculator = Calculator()
        if operator == '+':
            result = calculator.add(first_number, second_number)
        elif operator == '-':
            result = calculator.subtract(first_number, second_number)
        elif operator == '*':
            result = calculator.multiply(first_number, second_number)
        elif operator == '/':
            result = calculator.divide(first_number, second_number)
        else:
            raise ValueError("Invalid operator")
        return result

    def add(self, first_number: Union[int, float], second_number: Union[int, float]):
        return first_number + second_number
    
    def subtract(self, first_number: Union[int, float], second_number: Union[int, float]):
        return first_number - second_number
    
    def multiply(self, first_number: Union[int, float], second_number: Union[int, float]):
        return first_number * second_number
    
    def divide(self, first_number: Union[int, float], second_number: Union[int, float]):
        return first_number / second_number

calculator = Calculator()
result = calculator.get_numbers()
print(result)