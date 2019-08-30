"""
Prac 05 - Word Occurrences
"""

word_count = {}
text = input("Enter a string >")
words = text.split()
max_length = 0

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
    if len(word) > max_length:
        max_length = len(word)

words = list(word_count.keys())
words.sort()

for word in words:
    print("{:{}} : {}".format(word, max_length, word_count[word]))
