class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        # 1. 这个感觉更好一点
        
        res = 1
        
        while b:
            res = (res * (a ** b[-1])) % 1337
            b = b[:-1]
            a = (a ** 10) % 1337
        
        return res % 1337
        
        
        
        # 2. 这个都看不太懂了
        
        # if not b:
        #     return 1
        
        # last = b.pop()
        
        # tmp = self.superPow(a, b)
        # tmppow = 1
        # for i in range(10):
        #     tmppow = ((tmppow % 1337) * (tmp % 1337)) % 1337
        
        # apow = 1
        # for i in range(last):
        #     apow = ((apow % 1337) * (a % 1337)) % 1337
            
        # return (apow * tmppow) % 1337

# (2 ** 321) % 1337
# = [ (2 ** 1) % 1337 * [(2 ** 32) % 1337] ** 10 ]     % 1337




