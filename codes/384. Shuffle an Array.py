class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        tmp = self.nums[:]
        res = []
        while tmp:
            a = random.randint(0, len(tmp)-1)
            res.append(tmp[a])
            del tmp[a]
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()