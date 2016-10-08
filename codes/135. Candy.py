class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res = [1 for _ in range(len(ratings))]
        
        for i in range(1, len(res)):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        
        for i in range(len(res) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)
        
        return sum(res)