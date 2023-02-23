import logging

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# logging.debug("Hello World")
# logging.info("Hello World")
# logging.warning("Hello World")
# logging.error("Hello World")
# logging.critical("Hello World")


def add_few_numbers(a: int, b: int) -> int:
    logging.debug(f"Adding {a} and {b}")
    return a + b

add_few_numbers(1, 2)

# def money_collected(amount: float) -> None:
#     logging.info(f"Collecting {amount} Euros")
#     #doing something else
#     if amount == 0:
#         logging.warning("Expected amount to be positive")

        
# try:
#     #do some code
# except Exception as e:
#     logging.error(f"Error: {e}")

def emergency_exit(fatal_error: bool) -> None:
    if fatal_error:
        logging.critical(f'had to stop')
    
emergency_exit(True)
