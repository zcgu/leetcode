class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.lst = []
        self.next(candidates, target, 0, [])
        return self.lst
        
    def next(self, cs, t, pos, lst):
        if sum(lst) == t:
            self.lst.append(lst)
            return
        
        if pos >= len(cs):
            return
        
        if sum(lst) + cs[pos] <= t:
            self.next(cs, t, pos, lst + [cs[pos]])
        
        self.next(cs, t, pos + 1, lst)