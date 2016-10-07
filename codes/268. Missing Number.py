class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        
        s2 = (1 + len(nums)) * len(nums) / 2
        
        return s2 - s