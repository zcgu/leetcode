class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        return self.dfs(num, target, 1)
        
    def dfs(self, num, target, m):

        res = []
        for i in range(len(num) - 1, -1, -1):       # 必须从后往前，因为‘－’后面的括起来要变号。
            first, second = num[:i], num[i:]
            
            if len(second) > 1 and second[0] == '0': continue
            
            if first == '':                     # 特殊情况在这处理了，一般在开头和下面的循环用if处理。
                if int(second) * m == target:
                    res.append(second)
                continue
            
            # +
            for s in self.dfs(first, target - int(second) * m, 1):
                res.append(s + '+' + second)
            
            # -
            for s in self.dfs(first, target + int(second) * m, 1):
                res.append(s + '-' + second)
            
            # *
            for s in self.dfs(first, target, m * int(second)):
                res.append(s + '*' + second)
        
        return res
