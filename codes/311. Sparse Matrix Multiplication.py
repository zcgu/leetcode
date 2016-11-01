
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
        #1. 一个tableb，存b的行
        rowa = len(A)
        cola = rowb = len(B)
        colb = len(B[0])
        
        res = [[0 for _ in range(colb)] for _ in range(rowa)]
        
        tableb = {x:{} for x in range(rowb)}
        
        for x in range(rowb):
            for y in range(colb):
                if B[x][y] != 0:
                    tableb[x][y] = B[x][y]
        
        for x in range(rowa):
            for y in range(cola):
                if A[x][y] != 0:
                    for col in tableb[y]:
                        res[x][col] += A[x][y] * tableb[y][col]
        return res

#         2. 一个list存b的行，和上面基本一样
#         lstb = [[] for x in range(rowb)]
        
#         for x in range(rowb):
#             for y in range(colb):
#                 if B[x][y] != 0:
#                     lstb[x].append(y)
        
#         for x in range(rowa):
#             for y in range(cola):
#                 if A[x][y] != 0:
#                     for col in lstb[y]:
#                         res[x][col] += A[x][y] * B[y][col]
#         return res
    
    
