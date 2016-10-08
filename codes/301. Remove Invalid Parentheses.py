class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.visit = set()
        
        return self.dfs(s)
        
    def dfs(self, s):
        if s in self.visit: return []
        self.visit.add(s)
        
        num = self.cal(s)
        
        if num == 0: return [s]
        
        res = []
        
        for k in range(len(s) + 1):
            s2 = s[:k] + s[k+1:]
            
            if self.cal(s2) < num:
                res += self.dfs(s2)
        
        return res
        
                
    def cal(self, s):
        res = 0
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            
            if count < 0:
                res += 1
                count = 0
        return res + count
