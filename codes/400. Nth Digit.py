class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10: return n
        
        totalChar = 9
        n -= 1                      # 这个减一别忘了
        for i in range(2, 12):
            numChar = i * (10 ** (i - 1)) * 9
            if n <= totalChar + numChar:
                num = (n - totalChar) / i
                index = (n - totalChar) % i
                
                digit = 10 ** (i - 1) + num
                return int(str(digit)[index])
                
            totalChar += numChar