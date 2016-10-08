class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.dfs(n, n)
        
    def dfs(self, m, n):
        if m == 0 and n == 0: return ['']
        res = []
        
        if m > 0:
            for s in self.dfs(m - 1, n):
                res.append('(' + s)
        
        if n > m:
            for s in self.dfs(m, n - 1):
                res.append(')' + s)
        
        return res