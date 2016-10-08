class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                p1 = j + 1
                p2 = len(nums) - 1
                # print i ,j, p1, p2
                while p1 < p2:
                    sums = nums[i] + nums[j] + nums[p1] + nums[p2]
                    
                    if sums == target:
                        res.append([nums[i], nums[j], nums[p1], nums[p2]])
                        p1 += 1
                        p2 -= 1
                    elif sums < target:
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
        
        