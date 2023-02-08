# # Create a list of different types of python objects, and print all the types. The one who gets the the most unique types wins respect points:
# lst = [True, '15', 'fifteen', 15, {'fifteen' : 15}, 15.00, [15, 'fifteen'], (15, '15'), {15, '15', 'fifteen'}]
# for item in lst:
#     print(type(item))


# print(lst)

# # print all the items separated with "|"
# result = '|'.join(str(item) for item in lst)

# print(result)

# create a list of floats with 3 decimal points, create another list with all the values rounded to 2 decimals.
# second_lst = [2.177, 2.555, 6.777, 8.789]
# third_list = []
# for item in second_lst:
#     third_list.append(round(item, 2))
# # third_list_round = round(third_list)
# print(second_lst)
# print(third_list)

# # Create a list with student names and sort them, print the result to the terminal.
# fourth_list = ['Angela', 'Stan', 'David', 'Jack', 'Larry']
# fourth_list_sorted = sorted(fourth_list)
# print(fourth_list)
# print(fourth_list_sorted)


# write a program that allows user to write in any float number and then round it.
# question = input('Enter any number and how many decimals would you like?')
# split = question.split(" ")
# print(split)
# number = float(split[0])
# decimals = int(split[1])

# round_number = round(number, decimals)
# print(type(round_number))
# print(round_number)


# Create a program which would take 5 separate sentences containing 5 words.
# Make those sentences in separate lists and sort them out (reverse=False)
# Create 5 five new lists what would contain first, second  indexed elements from those lists. (first list containing
# all first elements of those five, second list second elements and so on).
# print the length of all list items and print the longest lenght list and shortest.


# sentences = [input(f"Enter sentence {i + 1}: ") for i in range(5)]
# # another way:
# # sentences = []
# # for i in range(5):
# #     sentence = input(f"Enter sentence {i + 1}: ")
# #     sentences.append(sentence)

# # spliting sentences into  words
# words = [sentence.split() for sentence in sentences]
# #another way:
# # words = []
# # for sentence in sentences:
# #     words.append(sentence.split())

# #using sort methon https://www.w3schools.com/python/ref_list_sort.asp 
# #it doesnt work
# sorted_words = sorted(words, reverse=False)
# print(sorted_words)

# # first lst from first elements and etc. https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
# lists = [[word[i] for word in words] for i in range(5)]

# # another way:
# # lists = []
# # for i in range(5):
# #   inside_list = []
# #   for word in words:
# #     inside_list.append(word[i])
# #   lists.append(inside_list)

# print(lists)