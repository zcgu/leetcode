class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums) - 1
        
        while l < r:
            while l < r - 1 and nums[l] == nums[l+1]:
                l += 1
            while l < r -1 and nums[r] == nums[r-1]:
                r -= 1
            
            
            mid = (l + r) / 2
            
            if nums[mid] == target:
                return True
            
            if nums[mid] < nums[l]:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return False if nums[l] != target else True
        