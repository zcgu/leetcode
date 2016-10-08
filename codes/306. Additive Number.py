class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        
            
        
        
        for i in range(1, len(num) + 1 - 1):
            for j in range(i + 1, len(num) + 1 - 1):
                if i != 1 and num[0] == '0' or j-i != 1 and num[i] == '0':
                    continue
                if self.dfs(num, int(num[:i]), int(num[i:j]), j):
                    return True
        return False
        
        
    def dfs(self, num, n1, n2, pos):
        # print n1, n2, pos
        if pos >= len(num):
            return True
            
        sums = str(n1 + n2)
        
        if int(num[pos:pos+len(sums)]) == n1 + n2:
            return self.dfs(num, n2, int(num[pos:pos+len(sums)]), pos+len(sums))
        
        else:
            return False