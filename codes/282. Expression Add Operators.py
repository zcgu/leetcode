class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # 这个题烦
        
        if not num: return []
        
        return self.dfs(num, target, 1, False)
        
    def dfs(self, num, target, m, isMulti):
        if not num:
            if isMulti and target == m:
                return ['']
            elif not isMulti and target == 0:
                return ['']
            else:
                return []
        
        res = []
        for i in range(len(num) - 1, -1, -1):   # 必须从后往前，因为‘－’后面的括起来要变号。
            a = num[i:]
            if len(a) > 1 and a[0] == '0':
                continue
            a = int(a)
            
            if i == 0:  # 特殊情况在这处理了，一般在下面的循环用if s：处理。这个题第三个是True，就不行了。
                for s in self.dfs(num[:i], target - a * m, 1, False):
                    res.append(num[i:])
                break
                
            for s in self.dfs(num[:i], target - a * m, 1, False):
                res.append(s + '+' + num[i:])
            
            for s in self.dfs(num[:i], a * m + target, 1, False):
                res.append(s + '-' + num[i:])
                
            for s in self.dfs(num[:i], target, a * m, True):
                res.append(s + '*' + num[i:])
            
        return res
