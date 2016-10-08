class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        if rowIndex == 0:
            return [1]
        
        res = [1]
        for i in range(1, rowIndex + 1):
            tmp = [0 for j in range(i+1)]
            
            tmp[0] = 1
            tmp[-1] = 1
            
            for j in range(1, i):
                tmp[j] = res[j-1] + res[j]
            
            res = tmp
        
        return res