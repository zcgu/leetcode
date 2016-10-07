class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = 1
        r = len(nums) - 1
        
        while l < r:
            mid = (l + r) / 2
            
            count = 0
            
            for num in nums:
                if l <= num <= mid: 
                    count += 1
            
            if count > mid - l + 1:     # this is key
                r = mid
            else:
                l =  mid + 1
        
        return l
        
        