class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
            
        res = ""
        
        i = 0
        while i < len(s):
            while not s[i].isdigit():
                res += s[i]
                i += 1
                if i >= len(s):
                    return res
            
            dstart = i
            while s[i].isdigit():
                i += 1
                
            digit = int(s[dstart: i])
            
            start2 = i
            count = 1
            i += 1
            while count > 0:
                if s[i] == '[':
                    count += 1
                elif s[i] == ']':
                    count -= 1
                i += 1
            
            substr = self.decodeString(s[start2+1: i-1])
            
            for _ in range(digit):
                res += substr
        return res