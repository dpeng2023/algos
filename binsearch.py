"""
Given:  Sorted List of numbers
Find:   Index Position of specified number, or return -1 if not found
Use:    Recursive and Iterative Binary Search
"""

# TEST#1:  [2, 5, 6, 7, 9], Find 7; Result 3
# TEST#2:  same as above, but Find 3; Result -1
# TEST#3:  same as above, but Find 1; Result -1
# TEST#4:  same as above, but find 10; Result -1
# TEST#5:  same as above, but find 9; Result 4
# TEST#6:  same as above, but find 2; Result 0
# TEST#7:  same as above, but find 6; Result 2

def ibinsearch(data: list, start: int, end: int, num: int) -> int:

    while end >= start:

        # find mid using integer division
        mid = start + (end - start)//2
        print("Start, End, Mid:  ", start, end, mid)

        if num == data[mid]:
            return mid
        elif num > data[mid]:
            # iterate start beyond mid
            start = mid + 1
        else:
            # iterate end beyond mid
            end = mid - 1

    return -1


def rbinsearch(data: list, start: int, end: int, num: int) -> int:

    # test for termination case
    if end >= start:

        # find mid using integer division
        mid = start + (end - start)//2
        print("Start, End, Mid:  ", start, end, mid)

        if num == data[mid]:
            return mid
        elif num > data[mid]:
            # iterate start beyond mid
            start = mid + 1
        else:
            # iterate end beyond mid
            end = mid - 1

        # return recursive call
        return rbinsearch(data, start, end, num)
    else:
        print("Terminating Recursion with Start, End", start, end)
        return -1


def find(data: list, num: int) -> int:
    end = len(data) - 1
    start = 0
    # foundIndex = rbinsearch(data, start, end, num)
    foundIndex = ibinsearch(data, start, end, num)
    return foundIndex

# TEST#1:  [2, 5, 6, 7, 9], Find 7; Result 3
input = [2, 5, 6, 7, 9]
print("\n***TEST#1:")
foundIndex = find(input, 7)
print("Found index:  ", foundIndex)

# TEST#2:  same as above, but Find 3; Result -1
print("\n***TEST#2:")
foundIndex = find(input, 3)
print("Found index:  ", foundIndex)

# TEST#3:  same as above, but Find 1; Result -1
print("\n***TEST#3:")
foundIndex = find(input, 1)
print("Found index:  ", foundIndex)

# TEST#4:  same as above, but find 10; Result -1
print("\n***TEST#4:")
foundIndex = find(input, 10)
print("Found index:  ", foundIndex)

# TEST#5:  same as above, but find 9; Result 4
print("\n***TEST#5:")
foundIndex = find(input, 9)
print("Found index:  ", foundIndex)

# TEST#6:  same as above, but find 2; Result 0
print("\n***TEST#6:")
foundIndex = find(input, 2)
print("Found index:  ", foundIndex)

# TEST#7:  same as above, but find 6; Result 2
print("\n***TEST#7:")
foundIndex = find(input, 6)
print("Found index:  ", foundIndex)
