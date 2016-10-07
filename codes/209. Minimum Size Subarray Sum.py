class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = 2 ** 31 - 1
        
        p1 = p2 = 0
        
        tmpSum = 0
        
        while p2 < len(nums):
            tmpSum += nums[p2]
            p2 += 1
            
            while tmpSum >= s:
                res = min(res, p2 - p1)
                
                tmpSum -= nums[p1]
                p1 += 1
        
        return res if res != 2 ** 31 - 1 else 0