class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 2:
            return list(set(nums))
            
        res = []
        
        cur1 = nums[0]
        cur2 = nums[1]
        count1 = 0
        count2 = 0
        
        for num in nums:
            if cur1 == num:
                count1 += 1
            elif cur2 == num:
                count2 += 1
            else:
                if count1 == 0:
                    cur1 = num
                    conut1 = 1
                elif count2 == 0:
                    cur2 = num
                    count2 = 1
                else:
                    count1 -= 1
                    count2 -= 1
        
        return [num for num in set([cur1, cur2]) if nums.count(num) > len(nums) / 3]