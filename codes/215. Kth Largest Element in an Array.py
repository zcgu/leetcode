class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        
        p1 = 0
        p2 = len(nums) - 1
        while True:
            index = self.partition(nums, p1, p2)
            
            if len(nums) - index == k:
                return nums[index]
            elif len(nums) - index < k:
                p2 = index - 1
            else:
                p1 = index + 1
    
    
    def partition(self, nums, a, b):
        if a >= b: return a
        
        p1, p2 = a, b
        mid = nums[a]
        
        while p1 < p2:
            while p1 < p2 and nums[p2] > mid:
                p2 -= 1
            nums[p1], nums[p2] = nums[p2], nums[p1]
            
            while p1 < p2 and nums[p1] <= mid:
                p1 += 1
            nums[p1], nums[p2] = nums[p2], nums[p1]
        
        nums[p1] = mid

        return p1












        # if not nums:
        #     return 0
            
        # from heapq import *
        
        # hp = []
        
        # for num in nums:
        #     if len(hp) < k or hp[0] < num:
        #         heappush(hp, num)
                
        #         if len(hp) > k:
        #             heappop(hp)
        
        # return hp[0]