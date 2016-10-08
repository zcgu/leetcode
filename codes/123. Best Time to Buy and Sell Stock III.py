class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        
        buy1 = buy2 = - 2 ** 31
        sell1 = sell2 = -2 ** 31
        
        for p in prices:
            if buy1  < 0     - p: buy1  = 0     - p
            if sell1 < buy1  + p: sell1 = buy1  + p
            if buy2  < sell1 - p: buy2  = sell1 - p
            if sell2 < buy2  + p: sell2 = buy2  + p
        
        return max(buy1, buy2, sell1, sell2)