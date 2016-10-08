class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        
        return len(nums)