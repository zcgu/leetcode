class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        
        res = []
        
        for num in set(nums1 + nums2):
            if num in set1 and num in set2:
                res.append(num)
        
        return res