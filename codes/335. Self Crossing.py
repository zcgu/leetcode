class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if len(x) < 4: return False
        
        a1 = a2 = a3 = a4 = a5 = a6 = 0
        
        for a1 in x:
            if a1 > 0 and a2 > 0 and a3 > 0 and a4 > 0 and \
                a3 <= a1 and a4 >= a2:
                    return True
            
            if a1 > 0 and a2 > 0 and a3 > 0 and a4 > 0 and a5 > 0 and\
                a3 <= a1 + a5 and a4 == a2:
                    return True
            
            
            if a1 > 0 and a2 > 0 and a3 > 0 and a4 > 0 and a5 > 0 and a6 > 0 and\
                a3 >= a1 and a4 >= a2 and a5 >= a3  - a1 and a5 <= a3 and a6 >= a4 - a2:
                    return True
        
            a2, a3, a4, a5, a6 = a1, a2, a3, a4, a5
        
        return False
            
            
            