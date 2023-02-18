# squares = []
# for number in range(10):
#     print(number)
#     if number == 5:
#         squares.append(number ** 2)
# print(squares)

# squares = [number ** 2 for number in range(10) if number == 5]
# print(f' second: {squares}')

# # We have five names
# names = ['John', 'Michael', 'Adam', 'Stewe', 'Luis']

# # for name in names:
# #     if len(name) >= 5:
# #         print(name)
# # print(names)

# #or

# names_list = [name for name in names if len(name) >= 5]

# print(names_list)

# my_smth = {
#     'Alpha': 1,
#     'Beta': 2,
# }

# squares = {i: i * i for i in range(1, 10) if i <= 6}
# print(squares)

# Create a dictionary with 5 key:value pairs. Keys must be strings and values must be numbers double digits(int).
# Use dictionary comprehension to create a dictionary where keys are the same keys as the current one just all capitalized.
# Values are in reverse order (25 -> 52).


# my_smth_one = {
#     'jordan': 23,
#     'kobe': 24,
#     'johnson': 32,
#     'nowitzki': 41,
#     'curry': 30,
# }


# # my_smth_two = {key.capitalize(): int(str(value)[::-1]) for key, value in my_smth_one.items()}

# # print(my_smth_two)

# my_new_dict = {}
# for name, number in my_smth_one.items():
#     my_new_dict[name.upper()] = int(str(number)[::-1])
# print(my_new_dict)
 

# values = ['a', 'b', 'c']
# values_two = {}
# for index, value in enumerate(values):
#     print(index, value)
#     values_two[value] = index + 1
# print(values_two) 

# names = ['John', 'Michael', 'Adam', 'Stewe', 'Luis']

# names_two = {index: name for index, name in enumerate(names)}
# print(names_two)

# names_dict = {}
# for index, name in enumerate(names):
#     names_dict[index] = name
# print(names_dict)

#Find all of the numbers from 1-1000 that are divisible by 6.

# for number in range(1, 1001):
#     if number % 6 == 0:
#         print(number)

# find_numbers = [print(number) for number in range(1, 1001) if (number % 6 == 0)]

# # Find all number from 1-1000 that have 9 in them.
# numbers = []
# for number in range(1, 1001):
#     if '9' in str(number):
#         numbers.append(number)
# print(numbers)


# # another version:
# find_numbers = [number for number in range(1, 1001) if '9' in str(number)]
# print(find_numbers)

#Given string: text = 'In this lecture we will review some additional functionalities of python built-in data structures.' calculate how many words have letter 'e' in it.
text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
words = text.split()
print(words)
count = 0

# for word in words:
#     if 'e' in word:
#         count += 1

# print(count)
count_letters = {}
for word in words:
    if len(word) >= 5:
        count_letters[word] = len(word)
print(count_letters)