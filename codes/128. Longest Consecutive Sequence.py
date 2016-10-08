class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        res = 0
        
        for num in nums:
            if num not in s:
                continue
            
            count = 1
            s.remove(num)
            
            left = num - 1
            while left in s:
                count += 1
                s.remove(left)
                left -= 1
            
            right = num + 1
            while right in s:
                count += 1
                s.remove(right)
                right += 1
            
            res = max(res, count)
            
        return res