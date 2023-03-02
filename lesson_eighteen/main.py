# class Names:
#     """This is the main class of the Antanas project. It contains all the functions that are used to"""

#     def __init__(self, name: str, surname: str, age: int) -> None:
#         self.name = name
#         self._surname = surname
#         self.__age = age
    
#     def print_out_name(self) -> None:
#         print(self.name)
#     def change_name(self, name: str) -> None:
#         self.name = name


# my_name = Names(name='Antanas', surname='Mindukas', age=22)

# my_name.change_name('Minde')


# # print(my_name.name)
# # print(my_name._surname)
# # print(my_name.__age)


# # # class Employee():

# class Car:
#     def __init__(self, color: str, cost: int, make_year: int) -> None:
#         self.make_year = make_year
#         self.cost = cost
#         self.color = color
#         self.full_info = f'{cost},{make_year},{color}'

#     def get_car_color(self) -> None:
#         print(f'My car is {self.color}')
    
#     def get_cost(self) -> float:
#         return self.cost
#     def get_make_year(self) -> int:
#         return self.make_year
#     def get_full_info(self) -> None:
#         print(f'My car is {self.full_info}')



class Car:
    def __init__(self, color: str, cost: int, make_year: int) -> None:
        self.make_year = make_year
        self.cost = cost
        self.color = color
        self.full_info = f'{cost},{make_year},{color}'

    def get_car_color(self, color: str) -> None:
        print(f'My car is {color}')

    def get_cost(self, cost: float) -> float:
        return self.cost

    def get_full_info(self, full_info: str) -> None:
        print(f'My car is {full_info}')

class Ferrari(Car):
    SPEED_CONSTANT = 20.5
    
    def __init__(self, hp: int) -> None:
        super().__init__()
        self.hp = hp

    def get_max_speed() -> float:
        return self.hp * SPEED_CONSTANT