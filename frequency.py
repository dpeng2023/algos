"""
Given a word input;
Print a frequency count for each vowel found

TEST #1: hitch-hiker
e was found 1 times.
i was found 2 times.

TEST #2: sky
No vowels found.
"""
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels:  ")

found = {}
for letter in word:
    if letter in vowels:
        # initializes first count for a new key value
        # first checks for key existence to initialize
        # otherwise would get KeyError on incrementing value for an unknown key
        # if letter not in found:
        #   found[letter] = 1
        # increments later count
        # else:
        #    found[letter] += 1
        # NOTE:  setdefault avoids having to pre-initialize all rows of dictionary
        found.setdefault(letter, 0)
        found[letter] += 1
# tests for empty set
if not found.keys():
    print('No vowels found.')
else:
    # sorts key, and parses out pair in hash table to key, value
    # otherwise iterator just iterates over keys in unordered form
    # sorted creates a COPY of the sorted keys to iterate over and is non-destructive
    for k,v in sorted(found.items()):
        print(k, 'was found', v, 'times.')