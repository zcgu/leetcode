# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
            
        res = 2
        
        for point in points:
            map = {}
            samep = 0
            
            for p in points:
                if p == point:
                    continue
                
                if p.x == point.x and p.y == point.y:
                    samep += 1
                elif p.x == point.x:
                    map[float('inf')] = map[float('inf')] + 1 if float('inf') in map else 1
                else:
                    k = (float(p.y) - float(point.y)) / (float(p.x) - float(point.x))
                    map[k] = map[k] + 1 if k in map else 1
                    
            if map:
                res = max(res, max(map.values()) + samep + 1)
            else:
                res = max(res, samep + 1)
        
        return res
                    