class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        money = [0, 0]
        
        for num in nums:
            money = [money[1] + num, max(money)]
        
        return max(money)