class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        res = self.msort(nums)

        nums[:] = res[:]
        
        
    def msort(self, nums):
        if len(nums) <= 1: return nums
        
        left = self.msort(nums[:len(nums)/2])
        right = self.msort(nums[len(nums)/2:])
        
        i = j = 0
        res = []
        
        while i < len(left) and j < len(right):
            if left[i]  < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        res += left[i:]
        res += right[j:]
        
        return res


#   1. quick sort
    #     self.qsort(nums, 0, len(nums) - 1)

    # def qsort(self, nums, a, b):
    #     if a >= b:
    #         return
        
    #     mid =  nums[a]
    #     p1 = a
    #     p2 = b
        
    #     while p1 < p2:
    #         while p2 > p1 and nums[p2] >= mid:
    #             p2 -= 1
    #         nums[p2], nums[p1] = nums[p1], nums[p2]
            
    #         while p1 < p2 and nums[p1] < mid:
    #             p1 += 1
    #         nums[p1], nums[p2] = nums[p2], nums[p1]
        
    #     nums[p1] = mid
    #     self.qsort(nums, a, p1-1)
    #     self.qsort(nums, p1 + 1, b)