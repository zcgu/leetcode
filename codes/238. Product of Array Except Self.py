class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1 for i in range(len(nums))]
        
        tmp = 1
        for i in range(len(nums) - 1):
            tmp *= nums[i]
            res[i+1] *= tmp
        
        tmp = 1
        for i in range(len(nums) - 1, 0, -1):
            tmp *= nums[i]
            res[i-1] *= tmp
        
        return res