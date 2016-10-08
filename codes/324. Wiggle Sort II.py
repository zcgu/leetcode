class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        mid, index = self.findKthLargest(nums, len(nums) / 2)
        index = self.threeWayPartition(nums, mid)
        
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        
        
    
    def threeWayPartition(self, nums, mid):
        i = j = 0
        n = len(nums) - 1
        
        while j <= n:
            if nums[j] > mid:
                nums[j], nums[n] = nums[n], nums[j]
                n -= 1
            elif nums[j] < mid:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
            else:
                j += 1
        
        return j

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        
        p1 = 0
        p2 = len(nums) - 1
        while True:
            index = self.partition(nums, p1, p2)
            
            if index == k:
                return nums[index], index
            elif index > k:
                p2 = index - 1
            else:
                p1 = index + 1
    
    
    def partition(self, nums, a, b):
        if a >= b: return a
        
        p1, p2 = a, b
        mid = nums[a]
        
        while p1 < p2:
            while p1 < p2 and nums[p2] > mid:
                p2 -= 1
            nums[p1], nums[p2] = nums[p2], nums[p1]
            
            while p1 < p2 and nums[p1] <= mid:
                p1 += 1
            nums[p1], nums[p2] = nums[p2], nums[p1]
        
        nums[p1] = mid

        return p1
