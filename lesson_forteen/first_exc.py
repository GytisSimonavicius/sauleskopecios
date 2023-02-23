# Create a simple program that would log all inputs from the terminal. Configs must show all additional data (time, date, level etc.)
import logging
logging.basicConfig(level=logging.DEBUG,filename='first_exc_data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
sex = input("Enter your sex(M/F): ")

logging.info(f"Person entered information. First name: {first_name}, Last name: {last_name}, Age: {age}, Sex: {sex}")
