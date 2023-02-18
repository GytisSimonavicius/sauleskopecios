# import time

# while True:
#     print('Zalgiris')
#     time.sleep(1)

# apples = 0

# while apples <= 10:
#     print(f'gathered apples so far: {apples}.')
#     apples += 1


# for letter in 'Antanas':
#     print(letter, end="")

# my_dict = {
#     'first_item': 1,
#     'last_item' : 2,
# }

# for key, value in my_dict.items():
#     print(f'Key: {key}, Value: {value}')

# my_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for _ in range(0, 5):
#     for number in my_number_list:
#         print(number)
#         if number >= 9:
#             break
#     print('___')
# # for x in range(0, 10):
# #     print(x)

my_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in my_number_list:
    if number == 7:
        continue
    print(number)
