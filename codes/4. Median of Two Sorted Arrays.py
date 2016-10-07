class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        lo = 0
        hi = m
        
        while lo <= hi:
            mid = (lo + hi) / 2
            
            mid2 = (m + n) / 2 - mid
            
            if mid - 1 >= 0 and mid2 < n and nums2[mid2] < nums1[mid-1]:
                hi = mid - 1
            elif mid2 - 1 >= 0 and mid < m and nums1[mid] < nums2[mid2-1]:
                lo = mid + 1
            else:
                
                # num1 = -2 ** 31
                # num2 = 2 ** 31 - 1
                if mid == 0:
                    num1 = nums2[mid2 - 1]
                elif mid2 == 0:
                    num1 = nums1[mid - 1]
                else:
                    num1 = max(nums1[mid-1], nums2[mid2-1])
                    
                if mid == m:
                    num2 = nums2[mid2]
                elif mid2 == n:
                    num2 = nums1[mid]
                else:
                    num2 = min(nums1[mid], nums2[mid2])
                
                if (m + n) % 2 == 0:
                    return (float(num1) + float(num2)) / 2
                else:
                    return num2