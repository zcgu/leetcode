class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix: return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        res = -2**31
        
        for left in range(n):
            sums = [0 for _ in range(m)]
            
            for right in range(left, n):
                
                for i in range(m):
                    sums[i] += matrix[i][right]
                
                # print left, right, sums
                
                tmp = self.helper(sums, k)
                res = max(res, tmp)
                
                # print tmp, res
                
        return res
    
    def helper(self, lst, k):
        res = -2 ** 31
        
        sums = [0]
        cursum = 0
        
        for num in lst:
            cursum += num
            
            from bisect import bisect_left, insort
            
            index = bisect_left(sums, cursum - k)
            if index < len(sums):
                res = max(res, cursum - sums[index])
            # print sums, cursum, num - k, index
            
            index = bisect_left(sums, cursum)
            sums.insert(index, cursum)
        return res
        
                    
                        
                        
                        