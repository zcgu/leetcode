class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return []
            
        lst = [1]
        
        for _ in range(1, n):
            
            num = lst[-1]
            
            if num * 10 <= n:
                lst.append(num * 10)
                continue
            
            num += 1
            while num % 10 == 0:
                num /= 10
            
            while num > n:
                num = num / 10 + 1
            
            lst.append(num)
            
        return lst