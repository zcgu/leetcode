class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    #     self.lst = []
    #     self.next(nums, 0, [])
    #     return self.lst
        
    # def next(self, nums, i, lst):
    #     if i >= len(nums):
    #         self.lst.append(lst)
    #         return
        
    #     self.next(nums, i + 1, lst)
    #     self.next(nums, i + 1, lst + [nums[i]])
    
        res = [[]]
        for num in nums:
            for i in range(len(res)):
                res.append(res[i] + [num])
        return res