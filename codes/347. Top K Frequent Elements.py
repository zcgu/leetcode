class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        
        lst = map.items()
        
        lst.sort(key=lambda l: l[1])
        
        res = []
        for i in range(k):
            res.append(lst[-1-i][0])
        return res