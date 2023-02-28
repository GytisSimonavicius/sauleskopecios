from typing import Union
class Country:
    def __init__(self, name: str, population: int, area: Union[int, float]) -> 'Country':
        self.name = name
        self.population = population
        self.area = area
    
    def is_big(self) -> bool:
        if self.population > 20000000 or self.area > 3000000:
            return True
        else:
            return False


    def compare_pd(self, other_country):
        density = self.population / self.area
        other_density = other_country.population / other_country.area
        if density < other_density:
            return f"{self.name} has a smaller population density than {other_country.name}"
        elif density > other_density:
            return f"{self.name} has a larger population density than {other_country.name}"
        else:
            return f"{self.name} has the same population density as {other_country.name}"

australia = Country('Australia', 2354550, 7692024)
andorra = Country('Andorra', 76098, 468)

print(bool(australia.is_big()))
print(bool(andorra.is_big()))

print(australia.compare_pd(andorra))