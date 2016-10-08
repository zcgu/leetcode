class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        
        money = [nums[0], 0]    # rob第一个，则不能rob最后一个
        for num in nums[1:]:
            money = [num + money[1], max(money)]
        res1 = money[1]
        
        money = [0, 0]      # 不rob第一个，则能rob或不rob最后一个
        for num in nums[1:]:
            money = [num + money[1], max(money)]
        res2 = max(money)
        
        return max(res1, res2)