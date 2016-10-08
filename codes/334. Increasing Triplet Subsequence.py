class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min1 = 2 ** 31 - 1
        min2 = 2 ** 31 - 1
        
        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            else:
                return True
        
        return False