# Write a function that moves all elements of one type to the end of the list:

# move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# # Move all the 1s to the end of the array.
import logging
logging.basicConfig(level=logging.DEBUG,filename='second_exc.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

def move_to_end(lst: list, element: int) -> list:
    count = lst.count(element)
    lst = [x for x in lst if x != element]
    lst += [element] * count
    return lst

move = move_to_end([1, 3, 2, 4, 4, 1], 1)

logging.debug(move)
