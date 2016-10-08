class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        f0 = 0
        for i in range(len(A)):
            f0 += i * A[i]
        
        sumA = sum(A)
        
        lastIndex = len(A) - 1
        
        maxF = f0
        
        for i in range(1, len(A)):
            fnew = f0 + sumA - A[lastIndex] * (len(A))
            maxF = max(maxF, fnew)
            f0 = fnew
            lastIndex -= 1
        
        return maxF