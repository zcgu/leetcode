class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 还是dp[start][end],然后从长度开始dp，k遍历最后一个爆的气球。
        
        if not nums: return 0
        
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        
        for length in range(len(nums) - 2):     # 上限不重要
            for start in range(1, len(nums) -1):    # 这个range重要
                end = start + length
                
                if end >= len(nums) - 1: continue   # 这个range重要
            
                for k in range(start, end + 1):
                    dp[start][end] = max(dp[start][end], \
                        nums[k] * nums[start-1] * nums[end +1] + dp[start][k-1] + dp[k+1][end])
        
        return dp[1][len(nums) - 2]