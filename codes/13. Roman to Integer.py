class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # I, II, III, IV, V, VI, VII, VIII, IX, X. 从右往左变大，变小的那个要减去
        
        table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        res = 0
        
        i = len(s) - 1
        while i >= 0:
            if  i > 0 and table[s[i]] > table[s[i - 1]]:
                res += table[s[i]] - table[s[i - 1]]
                i -= 2
            else:
                res += table[s[i]]
                i -= 1
        
        return res
            
