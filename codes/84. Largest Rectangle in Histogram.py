class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        hs = heights + [0]
        
        stack = []
        res = 0
        
        for i, h in enumerate(hs):
            while stack and h < hs[stack[-1]]:
                index = stack.pop()
                
                left = -1 if not stack else stack[-1]    # interesting part, this left index is left of lst[-1]
                
                res = max(res, hs[index] * (i - (left + 1)))
                
            stack.append(i)

        return res