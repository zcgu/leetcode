class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # 1. 不用count，更简单一点。
        
        res = ''
        p1 = p2 = 0
        
        table = {c: t.count(c) for c in t}
        
        while p2 < len(s):
            if s[p2] in table:
                table[s[p2]] -= 1
            p2 += 1
            
            while p1 < p2 and max(table.values()) <= 0:
                if res == '' or len(res) > p2 - p1:
                    res = s[p1:p2]
                if s[p1] in table:
                    table[s[p1]] += 1
                p1 += 1
        return res
        
        

# 2. 用一个count
        # table = {}
        # p1 = 0
        # p2 = 0
        # count = 0
        # res = ''
        
        # for c in t:
        #     table[c] = table[c] + 1 if c in table else 1
        
        # while p2 < len(s):
        #     if s[p2] in table:
        #         table[s[p2]] -= 1
                
        #         if table[s[p2]] >= 0:
        #             count += 1
            
        #     p2 += 1
            
        #     while count == len(t):
        #         # print p1, p2
        #         res = s[p1:p2] if len(res) > len(s[p1:p2]) or res == '' else res
                
        #         if s[p1] in table:
        #             table[s[p1]] += 1
                    
        #             if table[s[p1]] > 0:
        #                 count -= 1
                
        #         p1 += 1
        
        # return res
                
                
        
        