class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
            
        nums.sort()
        
        res = sum(nums[:3])
        
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                
                if abs(sums - target) < abs(res - target):
                    res = sums
                
                if sums < target:
                    j += 1
                else:
                    k -= 1
        return res
                
                
                