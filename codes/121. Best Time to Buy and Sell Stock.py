class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
            
        res = 0
        
        last = prices[0]
        for p in prices:
            if p > last:
                res = max(res, p - last)
            else:
                last = p
        
        return res
            