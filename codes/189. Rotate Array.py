class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
#         gcd方法，O（n）write，强无敌
        if k == 0 : return
        
        k %= len(nums)
        g = self.gcd(k, len(nums))
        
        for p in range(g):
            last = nums[p]
            for _ in range(len(nums) / g):
                p = (p + k) % len(nums)
                nums[p], last = last, nums[p]

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        
        return a
        
        

# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         k = k % len(nums)
        
#         mid = len(nums) - k
        
#         p1 = 0
#         p2 = mid - 1
#         while p1 < p2:
#             nums[p1], nums[p2] = nums[p2], nums[p1]
#             p1 += 1
#             p2 -= 1
        
#         p1 = mid
#         p2 = len(nums) - 1
#         while p1 < p2:
#             nums[p1], nums[p2] = nums[p2], nums[p1]
#             p1 += 1
#             p2 -= 1
        
#         p1 = 0
#         p2 = len(nums) - 1
#         while p1 < p2:
#             nums[p1], nums[p2] = nums[p2], nums[p1]
#             p1 += 1
#             p2 -= 1
        
