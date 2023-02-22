# Create a function that takes one parameter as number - age , other as name which is default 'Anatnas', and some args and keywords.
# Print first Name with age;
# And then print all arguments with key arguments.

# def print_name_age_with_arguments(age: int , name: str='Antanas', *args, **kwargs) -> None:
#     print(f'This is {name} and he is {age} years old')
#     print(f'free arguments: {args if args else "no arguments"}, free keyword arguments: {kwargs if kwargs else "no keyword arguments"}') 
# print_name_age_with_arguments(10)
# print_name_age_with_arguments(69, 'jurgis', (8, 9, 8))
# print_name_age_with_arguments(69, 'jurgis', 'john', 'steve', 'john', last_name = 'Simmons')


#Error handling
# from typing import Union

# def divider(number: Union[float, int]) -> Union[float, int]:
#     return number / 2 if isinstance(number, int) else number // 2


# # try: 
# #     my_division = divider(10)
# #     my_division_two = divider('algis')
# #     print(my_division)
# #     print(my_division_two)

# # except TypeError:
# #     print('Error')
# # except ZeroDivisionError:
# #     print('Never divide by 0')

# try:
#     my_division = divider(5)
#     print(my_division)
# except Exception as e:
#     print(f'Error: {e}')
# from typing import Optional, Union

# # try:
# #     def physics_is_fun(temp: float, pressure: float, time: int, weight: float) -> None:
# #         pass
# #     physics_is_fun(temp= 30.03, pressure= 1013.25, time= 100, weight= 450.4)
# #     print(f'Just checking')

# # except Exception as e:
# #     print(f'Error: {e}')

# # finally:
# #     print('Done')

# def divider(number: Union[float, int]) -> Optional[Union[float, int]]:
#     try:
#        return number / 2 if isinstance(number,[Union[fl]]) else number // 2
#     except TypeError:
#         print('Wrong type received')
#     except Exception as e:
#         print(f'Error: {e}')
