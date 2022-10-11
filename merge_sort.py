"""
MERGESORT
- time complexity O(NlogN) as divide and conquer with linear merge step
- space complexity O(N) as copies into auxiliary arrays on merge
- divide list into Left and Right halves until sections of length 1 are reached
- merge left and right (sorted) halves by comparing head element and iterating appropriate half
- add remainder of half to the end of merged sorted list
"""


def merge(data: list, left: list, right: list):

    i = 0
    j = 0
    k = 0
    imax = len(left)
    jmax = len(right)

    # while bounded by sublists
    while (i < imax) and (j < jmax):
        # increment EITHER left or right index
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        # always increment merged index
        k += 1

    # process remainder of EITHER left or right sections
    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1


# recursive signature is just portion of list
def merge_sort(data: list):
    
    # terminate recursion if length of list is 1
    # print("Data Type1 is:  ")
    # print(type(data))
    if len(data) > 1:

        # integer division to find mid of the array
        mid = len(data)//2

        # use slice alias for left and right sides
        left = data[:mid]
        right = data[mid:]

        # print("Data Type2 is:  ")
        # print(type(left))
        merge_sort(left)
        merge_sort(right)

        merge(data, left, right)


def print_list(data: list):
    for i in range(len(data)):
        print(data[i], end=" ")
    print()


# Test Driver for merge function
"""
input = [38, 27, 43, 3, 9, 82, 10]
L = [27, 38, 43]
R = [3, 9, 10, 82]
print("Left data is:  ")
print_list(L)
print("Right data is:  ")
print_list(R)
merge(input, L, R)
print("Merged data is:  ")
print_list(input)
"""

# Test Driver for recursive mergesort function
input2 = [38, 27, 43, 3, 9, 82, 10]
print("Unsorted input data is:  ")
print_list(input2)
print("Sorted input data is:  ")
merge_sort(input2)
print_list(input2)


