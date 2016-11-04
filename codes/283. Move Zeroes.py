class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # p1 = p2 = 0
        # while p2 < len(nums):
        #     if nums[p2] == 0:
        #         p2 += 1
        #     else:
        #         nums[p1] = nums[p2]
        #         p1 += 1
        #         p2 += 1
        # while p1 < len(nums):
        #     nums[p1] = 0
        #     p1 += 1
            
       
       
#         p1 = p2 = 0
#         while p2 < len(nums):
#             if nums[p2] != 0:
#                 nums[p1], nums[p2] = nums[p2], nums[p1]
#                 p1 += 1
#                 p2 += 1
#             else:
#                 p2 += 1
#         return
    
       
        p1 = 0
        while p1 < len(nums) and nums[p1] != 0:
            p1 += 1
        
        p2 = p1
        while p2 < len(nums) and nums[p2] == 0:
            p2 += 1
        
        while p2 < len(nums):
            if nums[p2] != 0:
                nums[p1] = nums[p2]
                p2 += 1
                p1 += 1
            else:
                p2 += 1
        
        while p1 < len(nums):
            if nums[p1] != 0:
                nums[p1] = 0
            p1 += 1
        
        
        
