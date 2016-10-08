class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        numlist = list(num)
        
        for _ in range(k):
            if not numlist:
                break
            
            found = False
            for p in range(len(numlist) - 1):
                if numlist[p] > numlist[p+1]:
                    del numlist[p]
                    found = True
                    break
            if not found:
                del numlist[-1]
        
        res = ''.join(numlist)
        res = res.lstrip('0')
        
        if not res:
            return '0'
        else:
            return res