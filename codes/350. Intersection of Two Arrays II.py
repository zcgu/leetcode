class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        table1 = {num: nums1.count(num) for num in nums1}
        table2 = {num: nums2.count(num) for num in nums2}
        
        res = []
        
        for num in set(nums1 + nums2):
            if num in table1 and num in table2:
                res += [num for _ in range(min(table1[num], table2[num]))]
        
        return res