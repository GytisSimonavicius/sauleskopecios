# print('Hello world!', 'Antanas', sep=':')

# a = 'ALIBABA'
# print(type(a))


# money_list = ['a', 'c', 'd', 'b', 'antanas', 'Mindaugas']

# print(sorted(money_list), reverse=True)



# Create a console aplication which takes a sentence of at least 10 words.
# print word in reverse order


sentence = input("Enter a sentence with at least 10 words. ")

lst = sentence.split()

srt = sorted(lst, reverse=True)

length = len(lst)
print(length)

for item in srt:
    print(item, end="")


