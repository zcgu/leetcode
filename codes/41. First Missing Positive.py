class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i] >= 1 and nums[i] <= len(nums) and nums[i]-1 != i and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                
        for i in range(len(nums)):
            if nums[i]-1 != i:
                return i + 1
        return len(nums)+1
        