class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # split = s.strip(' ' ).split(' ')
        # res = ''
        # for i in range(len(split) - 1, -1, -1):
        #     if split[i]:
        #         res += split[i] + ' '
        # return res.rstrip(' ')
        
        s = s.strip(' ')
        
        i = 0
        while i < len(s) - 1:
            if s[i] == ' ' and s[i+1] == ' ':
                s = s[:i] + s[i+1:]
            else:
                i += 1
        
        s = s[::-1]
        
        p1 = 0
        p2 = 0
        
        while p2 < len(s):
            while s[p2] != ' ':
                p2 += 1
                if p2 >= len(s):
                    break
            s = s[:p1] + ''.join(reversed(s[p1:p2])) + s[p2:]
            
            p1 = p2 = p2 + 1
        return s
            
            
            