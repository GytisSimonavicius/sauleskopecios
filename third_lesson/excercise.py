# # 1)Write a python program that sums up all items in the list (all items are integers or floats in list, create a list yourself)

# lst = [1, 2, 4, 2.45, 2.77, 7]

# sum = 0
# for item in lst:
#     sum += item
# print(sum)

# # 2) Write a python program that multiplies all items in the list (all items are integers or floats in list, create a list yourself)

# second_list = [12.25, 17.99, 78.11, 60, 7.23]

# result = 1
# for item in second_list:
#     result *= item
# format_result = "{:.2f}".format(result)
# print(format_result)

# # 3) Write a python program that gets maximum value from the list (all items are integers or floats in list, create a list yourself) 
# # 5)Create two lists and add them together, make sure it works the way you want it to.
# second_list.extend(lst)
# print(second_list)

# maximum_value = max(second_list)
# print(maximum_value)

# # 4)Write a python program that concatenates all strings in the list (all items are strings, create a list yourself)
# another_list = ['Hyundai', 'Toyota', 'Chevrolet', 'Dodge']
# text = ""
# for car in another_list:
#     text += car
# print(text)

# 6)Write a python program that asks user to enter 3 integers and find the highest value entered.
# first_number = int(input("Could you type any number?"))
# second_number = int(input("Could you type another number?"))
# third_number = int(input("Could you type any number last time?"))

# highest = max(first_number, second_number, third_number)

# print("The highest value is", highest)

# 1. create 4 digit pin code that is either string or int
# 2. create brute force algorithm that finds the correct pin code.
# 3. print that code

pincode = "1234"

code = 0

while True:
    if code == int(pincode):
        print('Pincode' + str(code))
        break
    else:
        code += 1
