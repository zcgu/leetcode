class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                if i - map[nums[i]] <= k:
                    return True
                else:
                    map[nums[i]] = i
            else:
                map[nums[i]] = i
        return False