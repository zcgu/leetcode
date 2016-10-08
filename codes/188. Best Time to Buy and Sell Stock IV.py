class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k > len(prices) / 2:     # not necessary in interview.
            res = 0
            
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    res += prices[i] - prices[i-1]
            
            return res
            
            
            
        # 从这开始
        buy = [-2 ** 31 for _ in range(k + 1)]  # 初始化为这个
        sell = [0 for _ in range(k + 1)]
        
        for p in prices:
            for i in range(1, k + 1):
                if buy[i] < sell[i-1] - p:
                    buy[i] = sell[i-1] - p
                
                if sell[i] < buy[i] + p:        # 这里是buy[i],然而上面是sell[i-1]
                    sell[i] = buy[i] + p
        
        return max(max(buy), max(sell))