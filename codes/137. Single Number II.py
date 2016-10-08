class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0 for i in range(32)]
        
        for num in nums:
            for i in range(32):
                mask = 1 << i
                if mask & num != 0:
                    count[i] += 1
        
        res = int(0)
        for i in range(31):
            if count[i] % 3 != 0:
                res |= 1 << i
        
        i = 31
        if count[i] % 3 != 0:
            res -= 1 << 31
            
        return res
            
        