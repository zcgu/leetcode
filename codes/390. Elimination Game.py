class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        direction = True
        gap = 2
        
        while start < end:
            if direction:
                if (end - start) % gap == 0:
                    end -= gap / 2
                start += gap / 2    
            else:
                if (end - start) % gap == 0:
                    start += gap / 2
                end -= gap / 2
            
            direction = not direction
            gap *= 2
                
        return start