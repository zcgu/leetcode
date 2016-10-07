class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.strip(' ')
        
        lst = s.split('e')
        
        if len(lst) > 2: return False
        
        for i, s2 in enumerate(lst):
            if s2 and s2[0] == '+':
                s2 = s2[1:]
            if s2 and s2[0] == '-':
                s2 = s2[1:]
            if not s2: return False
            
            dot = False
            number = False
            
            for c in s2:
                if c == '.':
                    if dot: return False
                    elif i == 1: return False
                    else: dot = True
                elif ord(c) >= ord('0') and ord(c) <= ord('9'):
                    number = True
                else:
                    return False
            
            if not number:
                return False
                
        return True
                
                
                
        