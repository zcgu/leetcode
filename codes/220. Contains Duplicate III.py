class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        
        if k < 0 or t < 0: return False
        
        
        buckets = {}
        
        for i, num in enumerate(nums):
            b = num / ( t + 1)
            
            if b in buckets:
                return True
            if b - 1 in buckets and abs(num - buckets[b - 1]) <= t:
                return True
            if b + 1 in buckets and abs(num - buckets[b + 1]) <= t:
                return True
            
            buckets[b] = num
            
            if i >= k:
                del buckets[nums[i-k] / (t + 1)]
        
        return False
        
        
        
        
        
        
        
        
        
        # lst = [(nums[i], i) for i in range(len(nums))]
        
        # lst.sort()
        
        # for i in range(len(lst)):
        #     for j in range(i+1, len(lst)):
                
        #         if abs(lst[j][0] - lst[i][0]) <= t and abs(lst[j][1] - lst[i][1]) <= k:
        #             return True
                
        #         if abs(lst[j][0] - lst[i][0]) > t:
        #             break
        
        # return False
        
        