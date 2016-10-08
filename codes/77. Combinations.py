class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        res = [[]]
        
        for i in range(1, n + 1):
            for j in range(len(res)):
                if len(res[j]) < k:
                    res.append(res[j] + [i])
            
            
        return [lst for lst in res if len(lst) == k]
        
        
                
    #     self.res = []
    #     self.recur(n, k, 1, [])
    #     return self.res
        
    # def recur(self, n, k, num, lst):
    #     if len(lst) == k:
    #         self.res.append(lst)
    #         return
        
    #     for i in range(num, n+1):
    #         self.recur(n, k, i+1, lst + [i])