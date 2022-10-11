# Find all pairs with a given sum
#
# Input:  Two unsorted arrays A of size N, B of size M of distinct elements
#         Find all pairs from both arrays such that the sum is equal to X
#
# Solution:  O(n) complexity instead of O(nm)

def allPairs(A, B, N, M, X):
    bmatch = {}
    for i in B:
        bmatch[i] = 1
    for j in A:
        bfind = X - j
        if bfind in bmatch:
            print(j, bfind)


# TEST1
"""
A = [1, 2, 4, 5, 7]
B = [5, 6, 3, 4, 8]
X = 9
allPairs(A, B, 5, 5, X)
"""
# RESULT1
"""
1 8
4 5
5 4
"""

#TEST2
A = [-1, -2, 4, -6, 5, 7]
B = [6, 3, 4, 0]
X = 8
allPairs(A, B, 6, 4, X)
# RESULT2
"""
4 4
5 3
"""