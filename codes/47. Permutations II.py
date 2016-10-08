class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        nums.sort()
        self.res = []
        self.used = [False for i in range(len(nums))]
        self.dfs(nums, [])
        
        return self.res
        
    def dfs(self, nums, lst):
        if len(lst) == len(nums):
            self.res.append(lst)
            return
        
        for i, num in enumerate(nums):
            if self.used[i]:
                continue
            # important
            if i > 0 and num == nums[i-1] and not self.used[i-1]:   
                continue
            
            self.used[i] = True
            
            self.dfs(nums, lst+[num])
            
            self.used[i] = False
            
            
            
            