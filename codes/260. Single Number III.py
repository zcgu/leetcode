class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        allXOR = 0
        
        for num in nums:
            allXOR ^= num
        
        differLocation = 1
        
        while allXOR & differLocation == 0:
            differLocation *= 2
        
        res1 = 0
        res2 = 0
        
        for num in nums:
            if num & differLocation == 0:
                res1 ^= num
            else:
                res2 ^= num
        
        return [res1, res2]