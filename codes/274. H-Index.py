class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        c = citations
        if not c:
            return 0
        
        # c.sort()
        
        # h = 0
        # i = len(c) - 1
        
        # while c[i] > h and i >= 0:
        #     h += 1
        #     i -= 1
        
        # return h
        
        
        
        buckets = [0 for i in range(len(c) + 1)]
        
        for num in c:
            if num >= len(c):
                buckets[len(c)] += 1
            else:
                buckets[num] += 1
        
        sums = 0
        for i in range(len(buckets) - 1, -1, -1):
            sums += buckets[i]
            if sums >= i:
                return i
        return 0
        
        
        