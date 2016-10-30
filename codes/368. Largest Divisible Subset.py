class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        nums.sort()
        
        dp = [[nums[i]] for i in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) >= len(dp[i]):
                    dp[i] = dp[j][:] + [nums[i]]
        
        res = []
        for lst in dp:
            if len(lst) > len(res):
                res = lst
        return res
        

# 2. 这个略麻烦了

# class Solution(object):
#     def largestDivisibleSubset(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         # 先dp每个位置结尾的这个序列是多长，然后选最长的从后往前生成结果。
        
#         if not nums: return []
        
#         nums.sort()
        
#         dp = [1 for _ in range(len(nums))]
        
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[i] % nums[j] == 0:
#                     dp[i] = max(dp[i], dp[j] + 1)
        
        
#         # 生成结果部分
#         count = max(dp)
#         index = dp.index(count)
#         res = []
        
#         while count >= 1:
#             res.append(nums[index])
            
#             for i in range(index, -1, -1):
#                 if dp[i] == count - 1 and nums[index] % nums[i] == 0:
#                     index = i
#                     break
                
#             count -= 1
#         res.reverse()
#         return res
            
            
            
            
            
