class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        l = 0
        r = sum(nums)
        
        while l < r:
            mid = (l + r) / 2
            
            if self.isok(nums, m, mid):
                r = mid
            else:
                l = mid  +1
        
        return l
        
    def isok(self, nums, m, sums):
        count = 1
        tmpsum = 0
        
        for num in nums:
            if num > sums:
                return False
            
            if tmpsum + num > sums:
                count += 1
                tmpsum = num
            else:
                tmpsum += num
        
        return count <= m