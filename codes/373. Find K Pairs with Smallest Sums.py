from heapq import *
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
            
        hp = []
        
        for i in range(min(len(nums1), k)):
            heappush(hp, (nums1[i] + nums2[0], [i, 0]))
        
        res = []
        
        for _ in range(k):
            if len(hp) == 0:
                return res
            
            sums, pos = heappop(hp)
            i,j = pos
            res.append([nums1[i], nums2[j]])
            
            if j < len(nums2) - 1:
                heappush(hp, (nums1[i] + nums2[j+1], [i, j+1]))
        
        return res
            
            