class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # i = 1
        # while i < len(nums):
        #     if nums[i] != nums[0]:
        #         del nums[i]
        #         del nums[0]
        #         i = max(1, i - 1)
        #     else:
        #         i += 1
        # return nums[0]
        
        if not nums:
            return 0
            
        count = 0
        cur = nums[0]
        
        for num in nums:
            if count == 0:
                cur = num
                
            if cur == num:
                count += 1
            else:
                count -= 1
        
        return cur