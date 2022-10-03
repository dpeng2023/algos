"""
Given a word; find the unique vowels in the word
- Don't use a for...loop for comparisons
"""

def find_vowels(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    # word_set = set(list(word))
    word_set = set(word)
    found_vowels = vowels.intersection(word_set)
    print(found_vowels)
    # sorted set is a LIST type
    print('Found vowels are:  ', sorted(found_vowels))

print('TEST#1: hello; {e,o}')
word = 'hello'
find_vowels(word)
print(type(word))

print('\nTEST#2: sky; {}')
word = 'sky'
find_vowels(word)

print('\nTEST#3: hitch-hiker; {e,i}')
word = 'hitch-hiker'
find_vowels(word)
