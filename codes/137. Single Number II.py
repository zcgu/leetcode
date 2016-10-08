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
        
        res = 0
        for i in range(32):
            if count[i] % 3 != 0:
                res |= 1 << i
        
        return res if res <= 2 ** 31 - 1 else res - 2 ** 32     # 这个python真尼玛烦啊
            
        
