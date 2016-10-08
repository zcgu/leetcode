class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        k %= len(nums)
        
        tmp = []
        
        for i in range(len(nums) -k, len(nums)):
            tmp.append(nums[i])
        
        for i in range(len(nums) - 1, k - 1, -1):
            nums[i] = nums[i - k]
        
        for i in range(k):
            nums[i] = tmp[i]
        