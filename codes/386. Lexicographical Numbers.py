class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
#       13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
#       


        if n == 0:
            return []
            
        lst = [1]
        
        for _ in range(1, n):
            
            num = lst[-1]
            
            if num * 10 <= n:           # 1 -> 10
                lst.append(num * 10)
                continue
            
            num += 1                    # 10 -> 11, 2 -> 3
            while num % 10 == 0:        # 19 -> 20 -> 2
                num /= 10
            
            while num > n:              # 14 -> 2
                num = num / 10 + 1
            
            lst.append(num)
            
        return lst
