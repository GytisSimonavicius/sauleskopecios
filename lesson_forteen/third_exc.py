# Create 3 functions, that are related to each other (one is being called in another), and test all logger severity levels by your own design.
import logging

logging.basicConfig(level=logging.DEBUG,filename='third_exc_data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


def add_numbers(x, y):
    logging.info(f'Adding {x} and {y}')
    result = x + y
    logging.debug(f'Result is {result}')
    return result

def multiply_numbers(x, y):
    logging.info(f'Multiplying {x} and {y}')
    result = x * y
    logging.debug(f'Result is {result}')
    return result

def calculation(x, y):
    sum = add_numbers(x, y)
    multiply = multiply_numbers(x, y)
    final_result = sum * multiply
    logging.debug(f'{sum} * {multiply} result is {final_result}')
    logging.critical('This is a critical message')
    return final_result


if __name__ == '__main__':
    logging.debug('This is a debug message')
    calculation(2, 3)
