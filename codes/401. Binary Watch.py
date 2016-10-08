class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for k in range(num + 1):
            lst1 = self.dfs(k, 8)
            lst2 = self.dfs(num - k, 32)
            
            for time1 in lst1:
                for time2 in lst2:
                    if time1 >= 12 or time2 >= 60:  # 这个。。呃
                        continue
                    res.append(str(time1) + ':' + '0' * (2 - len(str(time2))) + str(time2))
        return res
        
    def dfs(self, num, maxnum):
        if num == 0: return [0]     # 这个结束是什么要搞清楚
        if maxnum == 0: return []
        
        res = []
        
        for time in self.dfs(num - 1, maxnum / 2):
            res.append(time + maxnum)
        
        for time in self.dfs(num, maxnum / 2):
            res.append(time)
        
        return res
