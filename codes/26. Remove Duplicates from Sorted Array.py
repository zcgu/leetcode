class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        
        while i + 1 < len(nums):
            if nums[i] == nums[i+1]:
                del nums[i+1]
            else:
                i += 1
        
        return len(nums)