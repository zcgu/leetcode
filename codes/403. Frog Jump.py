class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
    #     return self.next(stones, 0, 0)
        
        
        
    # def next(self, stones, i, just):
    #     if i == len(stones) - 1:
    #         return True
        
    #     for jump in [just-1, just, just+1]:
    #         for j in range(i+1, len(stones)):
    #             if stones[j] - stones[i] == jump:
    #                 if self.next(stones, j, jump):
    #                     return True
    #             if stones[j] - stones[i] > just + 1:
    #                 return False
    #             if stones[j] - stones[i] > jump:
    #                 break
        
    #     return False
        if not stones: return False
        
        table = {s: set() for s in stones}
        table[0] = set([0])
        table[1] = set([0])
        
        for s in stones[1:]:
            if len(table[s]) > 0:
                for last in table[s]:
                    for s2 in [s + s- last - 1, s +s- last, s +s- last + 1]:
                        if s2 != s and s2 in table:
                            table[s2].add(s)
        return len(table[stones[-1]]) > 0
                    
        
        
        
        
        
        
