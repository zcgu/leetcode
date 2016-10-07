class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp所有的ugly number。用一个index数组纪录每个ugly base该乘哪个了。
        
        ugly = [2, 3, 5]
        
        index = [0 for _ in range(len(ugly))]
        
        dp = [1]
        
        for _ in range(n - 1):
            curMin = 2 ** 31 - 1
            curI = -1
            
            for i in range(len(ugly)):
                while ugly[i] * dp[index[i]] <= dp[-1]:     # 这里别忘了，把index调整到目前的。
                    index[i] += 1
                
                if ugly[i] * dp[index[i]] < curMin:
                    curMin = ugly[i] * dp[index[i]]
                    curI = i
            
            dp.append(curMin)
            index[curI] += 1
        
        return dp[-1]