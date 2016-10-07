class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
            
        h = 0
        i = len(citations) - 1
        
        while citations[i] > h and i >= 0:  # this citations[i] > h not citations[i] >= h
            h += 1
            i -= 1
        
        return h