# ############################################################
# # first excercise
# # Create a program that allows user to Enter his/her name and Age
# # Calculate the year in which user was born
# # Print the answer to the Terminal

# name = input("What\' is your name?")
# age = input('What\' is your age?')

# year_of_birth = 2023 - int(age)

# print(name, " you were born in ", year_of_birth)
# ######################################################

# ######################################################
# # seconde excercise 
# # Create a program that allows user to enter a full sentence
# # print the sentence backwards
# # print every second letter in the sentence

# answer = input('Hello sir, how are you doing?')
# backwards = answer[::-1]
# every_second_letter = answer[::2]

# print(backwards)
# print(every_second_letter)
# ######################################################

# ######################################################
# # #third excercise

# # Create a program that expects user to enter two numbers
# # multiply those numbers and print the answer
# # Create similar programs with other signs.

# print("Hello Sir/Madam. I would like to ask you two random numbers.")
# first_number = input("Enter your first number ")
# second_number = input('Enter your second number ')
# multiply = int(first_number) * int(second_number)

# print(f'{first_number} * {second_number} = {multiply}')


#third excercise, part two

# Create a program that expects user to enter two numbers
# multiply those numbers and print the answer
# Create similar programs with other signs.

# print("Hello Sir/Madam. I would like to ask you two numbers.")
# first_number = input("Enter your first number ")
# second_number = input('Enter your second number ')
# multiply = int(first_number) / int(second_number)

# print(f'{first_number} / {second_number} = {int(multiply)}')
#########################################################


#fourth excercise
# Create program that allows user to enter text
# Convert that text to Leet speak 1337


leet_code = {"A" : "4",
	        "B" : "I3",
            "C" : "[",
            "D": "]",
            "E" : "3",
            "F" : "|=",
            "G" : "6",
            "H" : "#",
            "I" : "1",
            "J" : ",_|",
            "K": ">|",
            "L": "1",
            "M": "/\/\ ",
            "N": "^/",
            "O": "0",
            "P" : "|*",
            "Q": "(_,)",
            "R" : "I2",
            "S": "5",
            "T" : "7",
            "U" : "(_)",
            "V" : "\/",
            "W": "\/\/",
            "X" : "><",
            "Y" : "j",
            "Z" : "2"}

def replace_letter(text):
    leet_speak = ""
    for char in text:
        leet_speak += leet_code.get(char.upper(), char)
    print(leet_speak)
text = input('Hello, how you are you today?')

replace_letter(text)

