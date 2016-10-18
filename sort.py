#   1. quick sort

    def qsort(self, nums, a, b):
        if a >= b:
            return
        
        mid =  nums[a]
        p1 = a
        p2 = b
        
        while p1 < p2:
            while p2 > p1 and nums[p2] >= mid:
                p2 -= 1
            nums[p2], nums[p1] = nums[p1], nums[p2]
            
            while p1 < p2 and nums[p1] < mid:
                p1 += 1
            nums[p1], nums[p2] = nums[p2], nums[p1]
        
        nums[p1] = mid
        self.qsort(nums, a, p1-1)
        self.qsort(nums, p1 + 1, b)

        
#   2. merge sort

    def mergeSort(self, nums):
        if len(nums) <= 1: return nums
        
        nums1 = self.mergeSort(nums[:len(nums) / 2])
        nums2 = self.mergeSort(nums[len(nums) / 2:])
        
        res = []
        
        p1 = p2 = 0
        
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1
        
        res += nums1[p1:]
        res += nums2[p2:]
        
        return res
