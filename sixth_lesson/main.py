# Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.

# name = input('What\'s your name?')
# surname = input('What\'s your surname?')
# age = int(input('What\'s your age?'))

# if age >= 21:
#     print(f'Mr. {name} {surname}, welcome to Casino! Have an outstanding expierence!')
# else:
#     print(f'Sorry {name} {surname}, you are not allowed to enter our casino')

# Create a database (List of privileged users) print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"

# lst = ['John', 'Herbert', 'Stewe', 'Walker', 'Benjamin', 'Monica', 'Josh']
# person = input('Hello sir/maddad, what\'s your name?')
# if person in lst:
#     print(f'Hello {person}. Welcome to our casino. You are eligible to use VIP privilegies. Have a good evening!')
# else:
#     print('Welcome')

# allow user to enter two numbers, print out which one is higher than the other, or are they equal?

# first_num = int(input('Enter any number: '))
# second_num = int(input('Enter another number: '))

# if first_num > second_num:    
#     print(f'First number, which you entered ({first_num}), is higher than second number({second_num})')
# elif second_num == first_num:
#     print(f'Both numbers are equal ({first_num})')
# elif second_num > first_num:
#     print(f'First number, which you entered ({first_num}), is lower than second number ({second_num})')
# else:
#     print('Error')

# Write a small calculator application, that allows user to enter two numbers and a symbol, given and then do the operation and print an answer.
# first_num = float(input('Enter any number: '))
# second_num = float(input('Enter another number: '))
# sym = input('Enter operator symbol, which you would like to operate (*,/,+,-) ')

# if sym == '+':
#     result = first_num + second_num
# elif sym == '-':
#     result = first_num - second_num
# elif sym == '/':
#     result = first_num / second_num
# elif sym == '*':
#     result = first_num * second_num
# else:
#     print('Invalid operation')
#     result = None

# print(f'Result: {result}')

#create a number guessing game from 1-10, with random library. (IDEA FOR LATER MAYBE)
from random import randint

ran_num = print(randint(1, 10))
guess_num = int(input('Guess number from 1 to 10: '))
if ran_num == guess_num:
    print('Congratz, your guess is right!!!')
elif ran_num != guess_num:
    print('Ooops, wrong guess.. Try again.')
else:
    print('something wrong')
