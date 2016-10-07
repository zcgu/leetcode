class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = (l + r) / 2
            
            if nums[mid] == target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        if nums[l] != target:
            return [-1, -1]
            
        res = [l, 0]
        
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = (l + r) / 2 + 1
            
            if nums[mid] == target:
                l = mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid - 1
        
        res[1] = l
        return res
        
        