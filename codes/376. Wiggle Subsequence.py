class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        indp = [1 for _ in range(len(nums))]    # 以此num结尾的递增的序列长度
        dedp = [1 for _ in range(len(nums))]    # 以此num结尾的递减的序列长度
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    indp[i] = max(indp[i], 1 + dedp[j])
                if nums[i] < nums[j]:
                    dedp[i] = max(dedp[i], 1 + indp[j])
        
        return max(max(indp), max(dedp))