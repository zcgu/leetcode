class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1 = p2 = 0
        while p1 < len(nums):
            if nums[p1] == 0:
                p1 += 1
            else:
                nums[p2] = nums[p1]
                p1 += 1
                p2 += 1
        while p2 < len(nums):
            nums[p2] = 0
            p2 += 1
            
       
       
       
        # p1 = p2 = 0
        
        # while True:
            
        #     while p1 < len(nums) and nums[p1] != 0:
        #         p1 += 1
                
        #     if p1 >= len(nums):
        #         return
            
        #     # p2 = p1
        #     p2 = max(p1, p2)
            
        #     while p2 < len(nums) and nums[p2] == 0:
        #         p2 += 1
            
        #     if p2 >= len(nums):
        #         return
            
        #     nums[p1], nums[p2] = nums[p2], nums[p1]
            
        