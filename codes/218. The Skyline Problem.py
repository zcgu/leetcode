class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # [[p, h, isUP]]
        lines = []
        
        for b in buildings:
            lines.append([b[0], b[2], True])
            lines.append([b[1], b[2], False])
        
        lines.sort(key=lambda l: l[0])
        
        p = 0
        curh = 0
        res = []
        queh = []
        lasth = 0
        while p < len(lines):
            newh = 0
            
            if lines[p][2]:
                queh.append(lines[p][1])
            else:
                del queh[queh.index(lines[p][1])]
            
            p += 1
            
            while p < len(lines) and lines[p][0] == lines[p-1][0]:
                
                if lines[p][2]:
                    queh.append(lines[p][1])
                else:
                    del queh[queh.index(lines[p][1])]
                
                p += 1
            
            minh = max(queh) if queh else 0
            if minh != lasth:
                res.append([lines[p-1][0], minh])
            lasth = minh
        return res
            
            
            
            
            