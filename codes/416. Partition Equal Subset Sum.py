class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1: return False
        
        sums = sum(nums)
        if sums % 2 != 0: return False
        half = sums / 2
    
        for num in nums:
            if num == half: return True
            if num > half: return False
            
        return self.dfs(nums, half)
        
    def dfs(self, nums, sums):
        if sums < 0: return False
        
        if sums == 0:
            return True
        
        for i in range(len(nums)):
            if nums[i] <= sums:
                if self.dfs(nums[:i] + nums[i+1:], sums - nums[i]):
                    return True
        return False
        
        
