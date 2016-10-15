# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

# For example,
# Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.

# Note:
# Because the range might be a large number, the low and high numbers are represented as string.

class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        # 0, 1, 6, 8, 9
        if len(low) > len(high) or(len(low) == len(high) and low > high): return 0
        
        res = 0

        for i in range(len(low) + 1, len(high)):
            res += self.getCount(i, i)

        # len(low), len(high)

        if len(low) == len(high):
            lst = self.dfs(len(low), len(low))
            for s in lst:
                if high >= s >= low:
                    res += 1
            return res

        lst = self.dfs(len(low), len(low))
        for s in lst:
            if s >= low:
                res += 1
        
        lst = self.dfs(len(high), len(high))
        for s in lst:
            if s <= high:
                res += 1

        return res


    def getCount(self, n, maxn):
        if n == 0: return 1
        if n == 1: return 3
        
        return self.getCount(n -2, maxn) * (5 if n != maxn else 4)

    def dfs(self, n, maxn):
        if n == 0: return ['']
        if n == 1: return ['1', '8', '0']

        res = []
        for s in self.dfs(n - 2, maxn):
            table = {'1':'1', '8':'8', '6':'9', '9':'6'}
            if n != maxn: table['0'] = '0'
            
            for c in table:
                res.append(c + s + table[c])

        return res


