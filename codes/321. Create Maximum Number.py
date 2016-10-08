class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        # nums1 选i个，nums2 选k－i个，然后merge到一起，遍历所有i，选最大的。
        
        res = None
        
        for i in range(k+1):
            if i <= len(nums1) and k - i <= len(nums2):
                res1 = self.choose(nums1, i)
                
                res2 = self.choose(nums2, k - i)
                
                resm = self.merge(res1, res2)
                # print i, resm
                if not res or resm > res:
                    res = resm
                    # print res
        return res
    
    
    def choose(self, n, k):
        nums = n[:]
        p = 0
        
        while p < len(nums) - 1 and nums[p] >= nums[p+1]:   # >= rather than >. 相等的不删除，删除后面的
            p += 1
            
        for _ in range(len(nums) - k):
            del nums[p]
            p = max(0, p-1)
            
            while p < len(nums) - 1 and nums[p] >= nums[p+1]: # >= rather than >. 相等的不删除，删除后面的
                p += 1
        # print n, k, nums
        return nums
    
    def merge(self, nums1, nums2):
        return [max(nums1, nums2).pop(0) for _ in range(len(nums1) + len(nums2))]   # so nice
        
        
                
                