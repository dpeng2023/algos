
"""
    Reverse the words in a string
    - without use of split() function
    - minimal creation of new strings
    Given: The quick brown fox jumps
    Result: jumps fox brown quick The
"""

# reverses string from start, non-including the end index
def reverse_word(words:str, start:int, end:int) -> str:
    if (start == 0):
        # note cannot index one past zero to -1, so don't specify end here
        reversed_word = words[end-1::-1]
    else:
        # start -1 since end is one PAST end of the word
        reversed_word = words[end-1:start-1:-1]
    return reversed_word

def reverse_words(words:str) -> str:

    # reverse entire phrase
    reversed_phrase = words[::-1]
    reversed_words = []
    length = len(reversed_phrase)
    start = 0
    end = 0
    # now reverse each word between spaces
    for i in range(length):
        if (reversed_phrase[i] == ' '):
            # set end to one PAST end of the word
            end = i
            reversed_word = reverse_word(reversed_phrase, start, end)
            print("Reversed Word in Phrase is:  ", reversed_word)
            reversed_words.append(''.join(reversed_word))
            # iterate to next start
            start = end + 1
    # process final word
    end = length
    reversed_word = reverse_word(reversed_phrase, start, end)
    print("Last Reversed Word in Phrase is:  ", reversed_word)
    reversed_words.append(''.join(reversed_word))
    print("Reversed words in phrase are:  ", reversed_words)
    return ' '.join(reversed_words)

# TEST#1:  Reverse one word of phrase
words = "The quick brown fox jumps"
print("Original phrase is:  ", words)

print(words[::-1])
print(words[2:0:-1])
print(words[2::-1])
print(words[8:3:-1])
print(words[24:19:-1])

words_list = list(words)
first_reversed = reverse_word(words,0,3)
second_reversed = reverse_word(words,4,9)
last_reversed = reverse_word(words,20,25) # 25 is length of string, or one PAST the last index of 24
print("First reversed word is:  ", first_reversed)
print("Second reversed word is:  ", second_reversed)
print("Last reversed word is:  ", last_reversed)

reversed_phrase = reverse_words(words_list)
print("Reversed phrase is:  ", reversed_phrase)

