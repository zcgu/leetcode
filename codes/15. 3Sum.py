class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            p1 = i + 1
            p2 = len(nums) - 1
            
            while p1 < p2:
                sums = nums[i] + nums[p1] + nums[p2]
                if sums == 0:
                    res.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                elif sums < 0:
                    p1 += 1
                else:
                    p2 -= 1
        
        res.sort()
        i = 0
        while i < len(res) - 1:
            if res[i] == res[i+1]:
                del res[i+1]
            else:
                i += 1
        
        return res