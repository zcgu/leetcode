class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        
        while l < r:
            while l < r - 1 and nums[l] == nums[l+1]:
                l += 1
            while l < r - 1 and nums[r] == nums[r-1]:
                r -= 1
            

            mid = (l + r) / 2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid
            else:
                r = mid
        
        return nums[l]