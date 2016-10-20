# class Solution(object):
#     def canCross(self, stones):
#         """
#         :type stones: List[int]
#         :rtype: bool
#         """
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
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        table = {stone:set() for stone in stones}
        table[0].add(0)

        for stone in stones:
            for last in table[stone]:
                for jump in [last - 1, last, last + 1]:
                    if stone + jump in table and stone + jump != stone:
                        table[stone + jump].add(jump)
        return len(table[stones[-1]]) > 0
        
        
        
        
        
