class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        
        self.dfs(s, [])
        
        return self.res
        
    def dfs(self, s, lst):
        print s
        
        if not s:
            self.res.append(lst)
            return
        
        for i in range(1, len(s)+1):    # substring careful
            if self.isPartition(s[:i]):
                self.dfs(s[i:], lst + [s[:i]])
        
        
        
        
    def isPartition(self, s):
        p1 = 0
        p2 = len(s) - 1
        
        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
        