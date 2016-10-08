class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy，sell，cool是之前以buy，sell，和cool结尾的序列的最大值，不是当前位置结尾。
        
        if len(prices) < 2:
            return 0
            
        buy = [0 for i in range(len(prices))]
        sell = [0 for i in range(len(prices))]
        cool = [0 for i in range(len(prices))]
        
        buy[0] = -prices[0]
        sell[0] = 0
        cool[0] = 0
        
        for i in range(1, len(prices)):
            buy[i] = max(buy[i-1], cool[i-1] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            cool[i] = max(cool[i-1], sell[i-1], buy[i-1])   # 这有三个
        
        return max(buy[-1], sell[-1], cool[-1])