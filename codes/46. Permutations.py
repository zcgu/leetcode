class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.lst = []
        self.helper(nums, [])
        return self.lst
        
    def helper(self, nums, lst):
        if not nums:
            self.lst.append(lst)
            return
        
        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i+1:], lst + [nums[i]])