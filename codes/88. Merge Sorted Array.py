class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for _ in range(len(nums1) - m):
            del nums1[-1]
        for _ in range(len(nums2) - n):
            del nums2[-1]
            
        p1, p2 = 0, 0
        
        while p2 < len(nums2):
            if p1 < len(nums1) and nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                nums1.insert(p1, nums2[p2])
                p2 += 1
        
        return