class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxpos = 0
        for i, num in enumerate(nums):
            if maxpos < i:
                return False
            maxpos = max(i + num, maxpos)
            
        return True