class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        if not rectangles:
            return False
            
        minx = miny = 2 ** 31 - 1
        maxx = maxy = - 2 ** 31
        
        table = {}
        s = 0
        
        for r in rectangles:
            minx = min(minx, r[0], r[2])
            maxx = max(maxx, r[0], r[2])
            miny = min(miny, r[1], r[3])
            maxy = max(maxy, r[1], r[3])
            
            s1 = str(r[0]) + " " + str(r[1])
            s2 = str(r[2]) + " " + str(r[3])
            s3 = str(r[0]) + " " + str(r[3])
            s4 = str(r[2]) + " " + str(r[1])
            
            table[s1] = table[s1] + 1 if s1 in table else 1
            table[s2] = table[s2] + 1 if s2 in table else 1
            table[s3] = table[s3] + 1 if s3 in table else 1
            table[s4] = table[s4] + 1 if s4 in table else 1
            
            s += (r[2] - r[0]) * (r[3] - r[1])
        
        if s != (maxx - minx) * (maxy - miny):
            print 1
            return False
        
        s1 = str(minx) + " " + str(miny)
        s2 = str(maxx) + " " + str(maxy)
        s3 = str(maxx) + " " + str(miny)
        s4 = str(minx) + " " + str(maxy)
        
        if s1 not in table or table[s1] != 1:
            return False
        if s2 not in table or table[s2] != 1:
            return False
        if s3 not in table or table[s3] != 1:
            return False
        if s4 not in table or table[s4] != 1:
            return False
        
        del table[s1]
        del table[s2]
        del table[s3]
        del table[s4]
        
        for v in table.values():
            if v % 2 != 0:
                print v
                return False
        
        return True