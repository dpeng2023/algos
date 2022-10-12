
def sort012(arr, n):

    freq = [0,0,0]

    for i in arr:
        if i == 0:
            freq[0] += 1
        elif i == 1:
            freq[1] += 1
        else:
            freq[2] += 1

    # print('frequency:  ')
    # print(freq)

    sorted = []
    for i in range(0,3):
        for j in range(freq[i]):
            sorted.append(i)

    return sorted

"""
# TEST 1
# out:  [0, 0, 1, 1, 2, 2]
input = [0, 1, 2, 0, 1, 2]
output = sort012(input, len(input))
print(output)
"""

# TEST 2
# out:  [0, 0, 1, 2, 2]
input = [0, 2, 1, 2, 0]
output = sort012(input, len(input))
print(output)



