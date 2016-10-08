class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        res = [[]]
        lastl = lastl2 = 0
        for pos, num in enumerate(nums):
            lastl, lastl2 = lastl2, len(res)
            if pos > 0 and nums[pos] == nums[pos-1]:
                for i in range(lastl, len(res)):
                    res.append(res[i] + [num])
            else:
                for i in range(len(res)):
                    res.append(res[i] + [num])
            
        return res