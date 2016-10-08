class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = 0
        res = -2 ** 31
        
        for num in nums:
            curSum += num
            res = max(res, curSum)
            
            if curSum < 0:
                curSum = 0  
        
        return res