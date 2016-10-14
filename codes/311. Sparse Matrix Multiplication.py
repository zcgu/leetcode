
# Given two sparse matrices A and B, return the result of AB.

# You may assume that A's column number is equal to B's row number.

# Example:

# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]

# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]


#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |


class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        tableb = {}
        
        for x in range(len(B)):
            tableb[x] = {}
            for y in range(len(B[0])):
                if B[x][y] != 0:
                    tableb[x][y] = B[x][y]
        
        res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        
        for x in range(len(A)):
            for y in range(len(A[0])):
                if A[x][y] != 0:
                    for col in tableb[y]:
                        res[x][col] += A[x][y] * tableb[y][col]
        return res

