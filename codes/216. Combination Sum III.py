class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        
        self.recur(k, n, [], 0)
        
        return self.res
        
    def recur(self, k, n, l, suml):
        if len(l) == k and suml == n:
            self.res.append(l)
            return
        
        if len(l) == k or suml == n:
            return
        
        for i in range(l[-1] if l else 1, 10):
            if i not in l and suml + i <= n:
                self.recur(k, n, l + [i], suml + i)