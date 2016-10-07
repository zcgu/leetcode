class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        lst = [str(i) for i in range(1, n+1)]
        
        res = ''
        
        k-= 1
        
        while lst:
            n = math.factorial(len(lst) - 1)
            
            res += lst[(k) / n]
            
            del lst[(k) / n]
            
            k = k % n
            
        return res