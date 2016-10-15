# Given a list of numbers, a[0], a[1], a[2], … , a[N-1], where 0 <= a[i] < 2^32. Find the maximum result of a[i] XOR a[j].

# Could you do this in O(n) runtime?

# Input: [3, 10, 5, 25, 2, 8]
# Output: 28

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            res = (res << 1)
            tmp = set([num >> (31 - i) for num in nums])
            if any(res ^ 1 ^ num in tmp for num in tmp):
                res ^= 1
        return res
