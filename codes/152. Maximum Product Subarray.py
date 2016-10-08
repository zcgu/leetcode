class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        tmp = [nums[0], nums[0]]
        res = max(tmp)
        
        for num in nums[1:]:
            tmp = [max(tmp[0] * num, num, tmp[1] * num), min(tmp[0] * num, num, tmp[1] * num)]
            res = max(res, tmp[0])
        
        return res
        
        
        # p = 0
        # n = 0
        
        # res = - 2 ** 31
        
        # for num in nums:
        #     if p != 0:
        #         p *= num
        #     else:
        #         p = num
                
        #     if n != 0:
        #         n *= num
        #     else:
        #         n = num
            
        #     res = max(res, p, n)
            
        #     p, n = max(p, n), min(p, n)
            
        #     if p < 1:
        #         p = 0
            
        #     if n > -1:
        #         n = 0
                
        # return res
