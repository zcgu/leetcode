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
