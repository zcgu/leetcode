class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # lst = [0 for i in range(n+1)]
        
        # for turn in range(1, n+1):
        #     for i in range(1, n+1):
        #         if turn * i <= n:
        #             lst[turn * i] = 1 - lst[turn * i]
        #         else:
        #             break
        
        # return sum(lst)
        
        return int(math.sqrt(n))