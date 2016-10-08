class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        nums.sort()
        
        miss = 1
        i = 0
        count = 0
        
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                count += 1
                miss += miss
        
        return count
                