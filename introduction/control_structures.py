word_list = ['cat', 'dog', 'rabbit']

# print out list of all letters
# solution 1: using list comprehensions

print [word[i] for word in word_list for i in range(len(word))]
print [letter for letter in "".join(word_list)]

#solution 2: using loop and list method

letter_list = []

for word in word_list:
    for letter in word:
        letter_list.append(letter)

print letter_list

# print out all letters without duplicate
# solution 1: using list comprehensions

print list(set([word[i] for word in word_list for i in range(len(word))]))
print list(set([letter for letter in "".join(word_list)]))

# solution 2: using loop and if statement

letter_list = []

for word in word_list:
    for letter in word:
        if letter not in letter_list:
            letter_list.append(letter)

print letter_list
