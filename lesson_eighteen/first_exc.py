class Person:
    def __init__(self, first_name: str, last_name: str, age: int, personal_code: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__personal_code = personal_code

    def get_personal_code(self):
        return self.__personal_code

class Voter(Person):
    def __init__(self, first_name: str, last_name: str, age: int, personal_code: int):
        super().__init__(first_name, last_name, age, personal_code)

    def can_vote(self):
        return self.age >= 18

# Example usage
Gytis = Voter("Gytis", "Simonavicius", 27, "39501214545")
Liudas = Voter("Liudas", "Vasaris", 16, "12345678901")
print(Gytis.can_vote()) 
print(Liudas.can_vote())
