from random_word import RandomWords
r = RandomWords()

words = [r.get_random_word().upper() for _ in range(5)]
words.sort()

for word in words:
    print(word, end=" ")
