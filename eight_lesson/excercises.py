# Create a variables containing strings for username and password. 
# Start Endless loop allowing to enter username and password. 
# If credentials are correct stop endless loop and print greeting message.

# user_name = "admin"
# password = "admin"


# while True:
#     guess_name = input("Enter your username: ").lower()
#     gues_password = input("Enter your password: ").lower()
#     if gues_password == password and guess_name == user_name:
#         print(f"Welcome {user_name}. Hope you are doing well!")
#         break
#     else:
#         print("Incorrect username or password. Try again.")

#alternative version with lists
# credentials = ['admin', 'admin']
# while True:
#     guess_username = input("Enter your username and password separated by space: ").split(" ")
#     if guess_username[0] == credentials[0] and guess_username[1] == credentials[1]:
#         print(f"Welcome {guess_username[0]}. Hope you are doing well!")
#         break
#     else:
#         print("Incorrect username or password. Try again.")

# Allow user to enter 10 integers, and then print the sum and average of those entered numbers.

# numbers = []
# sum = 0

# for i in range(10):
#     number = int(input("Enter an integer: "))
#     numbers.append(number)
#     sum += number
# print(sum)
# average = sum / len(numbers)
# print(average)

# Generate a dictionary of 10 keys being 1,2,3...10 each of them should store a value of random integer number from 1 to 100.
# import random

# my_dict = {}
# for i in range(1,11):
#     my_dict[i] = random.randint(1, 100)

# print(my_dict)

# Create a list of letters and generate 5 diferent words for 5 different lists. (A word must the size between 5 and 15 letters)
# Then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}
# And all words sorted in one list.


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lst = []
words = []

for j in range(5):
    word = ''.join(random.choice(letters) for i in range(random.randint(5, 15)))
    words.append(word)    
    for i in range(5):
        lst.append(word)
print(lst)

$nebaigta