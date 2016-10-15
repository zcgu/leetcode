# Numbers can be regarded as product of its factors. For example,

# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and return all possible combinations of its factors.

# Note: 
# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.
# Examples: 
# input: 1
# output: 
# []
# input: 37
# output: 
# []
# input: 12
# output:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
# input: 32
# output:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]


class Solution(object):
    # 这题dfs有点特殊，不是在最后n＝＝1加，而是找到一个factor就记录结果。
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1: return []
        
        self.res = []
        
        lst = self.dfs(n, 2, [])
        return [l for l in self.res if len(l) != 1]
        
    def dfs(self, n, start, lst):
        
        if n == 1:
            return
        
        i = start
        while i * i <= n:
            if n % i == 0:
                self.res.append(lst + [i, n / i])   # a!
                self.dfs(n / i, i, lst + [i])
                
            i += 1
        
