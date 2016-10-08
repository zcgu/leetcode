class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.map = {}
        
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            if a in self.map:
               self.map[a][b] = values[i]
            else:
                map2 = {a: 1.0, b: values[i]}
                self.map[a] = map2
            if b in self.map:
                self.map[b][a] = 1.0 / values[i]
            else:
                map2 = {b: 1.0, a: 1.0 / values[i]}
                self.map[b] = map2
        
 
        
        lst = []
        for q in queries:
            self.v = [q[0]]
            lst.append(self.helper(q[0], q[1], 1.0))
        for i in range(len(lst)):
            if lst[i] is None:
                lst[i] = -1.0
        return lst
        
    def helper(self, a, b, num):
        if a not in self.map:
            return None
        
        for i in self.map[a]:
            if i == b:
                return num * self.map[a][i]
            
            if i not in self.v:
                self.v.append(i)
                tmp = self.helper(i, b, num * self.map[a][i])
                if tmp:
                    return tmp
        
        return None
            
            