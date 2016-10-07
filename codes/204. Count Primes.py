class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
            
        isPrime = [True for i in range(n)]
        
        isPrime[0] = False
        isPrime[1] = False
        
        i = 2
        while i**2 < n:
            if isPrime[i]:
                f = 2
                while f * i < n:
                    isPrime[f * i] = False
                    f += 1
            i += 1
        
        return isPrime.count(True)
            