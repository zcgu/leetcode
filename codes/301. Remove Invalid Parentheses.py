class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.visit = set()
        self.dfs(s)
        return self.res
    
    def dfs(self, s):
        num = self.cal(s)
        
        
        if num == 0 and s not in self.visit:
            self.res.append(s)
            self.visit.add(s)
            return
        
        self.visit.add(s)
        for i in range(len(s)):
            s2 = s[:i] + s[i+1:]
            
            if s2 not in self.visit and self.cal(s2) < num:
                self.dfs(s2)
        
    
    def cal(self, s):
        left = right = 0
        
        for c in s:
            if c == '(' or c == ')':
                left += 1 if c == '(' else -1
                right += left < 0
                left = max(left, 0)
                
        return left + right