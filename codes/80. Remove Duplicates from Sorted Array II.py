class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
            
        i = 1
        
        while i < len(nums) - 1:
            if nums[i] == nums[i-1] and nums[i] == nums[i+1]:
                del nums[i+1]
            else:
                i += 1
        
        return len(nums)