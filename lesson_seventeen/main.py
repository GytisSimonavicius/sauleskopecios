#classes
from datetime import date, datetime
class Person:
    description: str = 'A simple person class'

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def full_name(self) -> str:
        return f"{self.name} {self.surname}"
    
    # def calcutate_days_left_till_black_friday(self) -> int:
    #     #initialize today's date
    #     #initialize black friday's date
    #     #black friday - todays day
    #     black_friday = date(2023, 11, 24)
    #     today = date.today()
    #     delta = black_friday - today

    #     return delta.days

    def get_eye_color(self, eye_color: str) -> str:
        return eye_color

    def __repr__(self) -> str:
        return f"Person: {self.name} {self.surname}"


person = Person('Alex', 'Garcia')


# print(person.full_name())
# print(person.description)
print(person)
