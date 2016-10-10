class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0
        
        maxs = max(nums)
        mins = min(nums)
        
        l = len(nums)
        
        # gap是小数的话，最大gap的最小值就是向上取整。
        if (maxs - mins) % (l - 1) == 0:
            gap = (maxs - mins) / (l - 1)
        else:
            gap = (maxs - mins) / (l - 1) + 1 

        if gap == 0: return 0
        
        buckets = [(float('-inf'), float('inf')) for _ in range(len(nums))]
        
        for num in nums:
            index = (num - mins) / gap
            buckets[index] = (max(buckets[index][0], num), min(buckets[index][1], num))
        
        res = - 2 ** 31
        lastMax = None
        
        for b in buckets:
            if b[0] != float('-inf'):
                if lastMax is not None:
                    res = max(res, b[1] - lastMax)
                lastMax = b[0]

        return res
        
            
            
