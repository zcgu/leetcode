class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        self.res = []
        self.dfs(s, 0)
        return self.res
        
        
    def dfs(self, s, pos):
        if s.count('.') == 3:
            if self.valid(s[pos:]):
                self.res.append(s)
            return
        
        for i in range(pos + 1, min(len(s) + 1, pos + 4)):
            if self.valid(s[pos:i]):
                self.dfs(s[:i] + '.' + s[i:], i + 1)
    
    def valid(self, s):
        if len(s) >= 2 and s[0] == '0':
            return False
        
        return 0 < len(s) <= 3 and 0 <= int(s) <= 255
        
        
        
        