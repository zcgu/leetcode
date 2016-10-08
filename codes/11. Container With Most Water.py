class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h = height
        
        if len(h) <= 1:
            return 0
        
        res = (len(h) - 1 ) * min(h[0], h[-1])
        
        p1 = 0
        p2 = len(h) - 1
        
        while p1 < p2:
            res = max(res, (p2 - p1) * min(h[p1], h[p2]))
            
            if h[p1] > h[p2]:
                p2 -= 1
            else:
                p1 += 1
        
        return res
        