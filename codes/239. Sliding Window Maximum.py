class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deque = []
        res = []
        for i, num in enumerate(nums):
            if deque and deque[0] == i - k:
                deque.pop(0)
            while deque and nums[deque[-1]] < num:
                deque.pop()
            deque.append(i)
            if i >= k - 1:
                res.append(nums[deque[0]])
        return res