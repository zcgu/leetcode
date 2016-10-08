class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.res = []
        self.used = [False for i in range(len(candidates))]
        self.dfs(candidates, 0, target, [])
        

        return self.res
        
    def dfs(self, nums, i, target, lst):
        if sum(lst) == target:
            lst.sort()
            self.res.append(lst)
            return
        if sum(lst) > target:
            return
        
        if i >= len(nums):
            return
        
        self.dfs(nums, i+1, target, lst)
        
        if i > 0 and nums[i] == nums[i-1] and not self.used[i-1]:
            return
        
        self.used[i] = True
        self.dfs(nums, i+1, target, lst + [nums[i]])
        self.used[i] = False