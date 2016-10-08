class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp = [2**31 -1 for _ in range(len(nums))]
        
        # dp[0] = 0
        
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[j] >= i - j:
        #             dp[i] = min(dp[i], dp[j] + 1)
        
        # return dp[-1]
        
        count = 0
        curmax = 0
        mx = 0
        
        for i in range(len(nums) - 1):
            mx = max(mx, i + nums[i])
            
            if i == curmax:
                count += 1
                curmax = mx
        
        return count
            
        