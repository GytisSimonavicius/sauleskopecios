name = input("What\' is your name?")
age = input('What\' is your age?')

greeting = f"Hello {name}, I guess your age is {age}"

print(greeting)

age = int(age) + 1

print(f"And next year you will be {age} years old")