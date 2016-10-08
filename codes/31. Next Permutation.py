class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = -1
        for i in reversed(range(1, len(nums))):
            if nums[i] > nums[i-1]:
                pos = i
                break
        print pos
        if pos == -1:
            nums.sort()
            return
        
        minpos = -1
        minnum = 2 ** 31 - 1
        
        for i in range(pos, len(nums)):
            if nums[i] > nums[pos-1] and nums[i] < minnum:
                minnum = nums[i]
                minpos = i
        
        nums[pos-1], nums[minpos] = nums[minpos], nums[pos-1]
        
        nums2 = nums[pos:]
        nums2.sort()
        for i in range(len(nums2)):
            nums[i+pos] = nums2[i]
        
        
        