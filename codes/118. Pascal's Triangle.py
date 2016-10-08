class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
            
        if numRows == 1:
            return [[1]]
        
        res = [[1]]
        
        for i in range(2, numRows+1):
            tmp = [0 for j in range(i)]
            tmp[0] = 1
            tmp[-1] = 1
            
            for j in range(1, i-1):
                tmp[j] = res[i-2][j-1] + res[i-2][j]
            
            res.append(tmp)
        
        return res