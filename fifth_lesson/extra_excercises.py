# We have 3 dictionaries :  dic_one={1:10, 2:20} dic_two={3:30, 4:40} dic_three={5:50,6:60}
# Create one final dictionary from all those 3.
# dic_one = {
#     1: 10,
#     2: 20
# }
# dic_two = {
#     3: 30,
#     4: 40
# }
# dic_three = {
#     5: 50,
#     6: 60
# }

# dic_one.update(dic_two)
# dic_one.update(dic_three)

# # final_dict = {}
# # final_dict.update(dic_one)
# # final_dict.update(dic_two)
# # final_dict.update(dic_three)

# print(dic_one)


# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x):
# You can use input to receive the number. Example:
# n= 5 , output:  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


#enter how many items would you like in your dictionary
n = int(input('Enter how many items would you like to store in dictionary'))

#creating an empty dictionary
x_times_x_dict = {}

#creating for loop 
for x in range(1, n+1):
    x_times_x_dict[x] = x*x
print(x_times_x_dict)

#another way
