
# #Try creating structure like one here: link from an empty dictionary: my_dict = {} 

# #creating an empty dictionary
# my_dict = {}
# #assign student name value
# my_dict['student_name'] = 'John'
# #assign student surname value
# my_dict['student_surname'] = 'Williams'

# #creating another dictionary called grades, which stores student grades in different lectures
# grades = {
#     'math': 8,
#     'chemistry': 9,
#     'physics': 5   
# }

# #assign student grades to primary dictionary 
# my_dict['student_grades'] = grades

# #creating another dictionary called math, which stores student grades in specific mathematics

# math = {
#     'Number_teory': 10,
#     'Geometry': 10,
#     'Algebra': 5,
#     'Calculus': 6,
#     'Discrete_mathematics': 'fail'

# }
# #assign specific math grades to math dictionary 
# my_dict['student_grades']['math'] = math

# #just checking if anything is stored
# print(my_dict)

# #checking calculus grades
# calculus = my_dict['student_grades']['math']['Calculus']

# print(calculus)

#Write python program that asks user to enter name, surname, age. Put these values into a dictionary and print dictionary
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")

student = {
    "name": name,
    "surname": surname,
    "age": age
}

print(student)
