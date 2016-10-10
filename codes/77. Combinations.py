class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.dfs(n, k)
    
    def dfs(self, n, k):
        if k == 0: return [[]]
        if n == 0 or n < k: return []   # 加了一个小小的检查，就过了
        
        res = []
        for lst in self.dfs(n - 1, k):
            res.append(lst)
        for lst in self.dfs(n - 1, k - 1):
            res.append([n] + lst)
        
        return res
        
        # res = [[]]
        
        # for i in range(1, n + 1):
        #     for j in range(len(res)):
        #         if len(res[j]) < k:
        #             res.append(res[j] + [i])
            
            
        # return [lst for lst in res if len(lst) == k]
        
        
