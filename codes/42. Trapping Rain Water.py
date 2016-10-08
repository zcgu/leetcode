class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
            
        p1 = 0
        p2 = len(height) - 1
        last1 = height[0]
        last2 = height[-1]
        
        res = 0
        
        while p1 < p2:
            if height[p1] < height[p2]:
                p1 += 1
                if height[p1] < last1:
                    res += - height[p1] + last1
                else:
                    last1 = height[p1]
            else:
                p2 -= 1
                if height[p2] < last2:
                    res += - height[p2] + last2
                else:
                    last2 = height[p2]
        
        return res