class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = [0, 1]
        for i in range(n):
            ways = [ways[0] + ways[1], ways[0]]
        return sum(ways)