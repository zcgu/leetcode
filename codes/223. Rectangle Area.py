class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x1 = max(A, E)
        y1 = max(B, F)
        x2 = min(C, G)
        y2 = min(D, H)
        
        
        if x1 >= x2 or y1 >= y2: 
            middle = 0
        else:
            middle = (x2 - x1) * (y2 - y1)
            
        return (C- A) * (D - B) + (G - E) * (H - F) - middle
        
        
        