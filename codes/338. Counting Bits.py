class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # 太简单
        
        lst = [0]
        
        for i in range(1, num + 1):
            lst.append( lst[i/2] + i % 2 )
        
        return lst