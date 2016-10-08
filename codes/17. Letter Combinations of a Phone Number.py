class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.map = {'2': ['a', 'b', 'c'], '3' : ['d', 'e', 'f'], 
            '4':['g','h', 'i'], '5':['j','k','l'], '6':['m','n','o'],
            '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        
        if not digits:
            return []
        
    #     self.res = []
    #     self.recur(digits, "")
    #     return self.res
    
    # def recur(self, digits, lst):
    #     if not digits:
    #         self.res.append(lst)
    #         return
        
    #     for c in self.map[digits[0]]:
    #         self.recur(digits[1:], lst + c)
    
        res = [""]
        for d in digits:
            tmp = []
            for c in self.map[d]:
                for r in res:
                    tmp.append(r + c)
            res = tmp
            
        return res
        