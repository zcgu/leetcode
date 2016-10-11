class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        mid = len(nums) - k
        
        p1 = 0
        p2 = mid - 1
        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 -= 1
        
        p1 = mid
        p2 = len(nums) - 1
        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 -= 1
        
        p1 = 0
        p2 = len(nums) - 1
        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 -= 1
        
