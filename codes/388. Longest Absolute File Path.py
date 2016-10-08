class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        table = {0: 0}
        p = 0
        res = 0

        while p < len(input):
            if p < len(input) and input[p] == '\n':
                p += 1
            
            lvl = 1
            
            while p < len(input) and input[p] == '\t':
                p += 1
                lvl += 1
            
            length = 0
            isFile = False
            while p < len(input) and input[p] != '\n':
                length += 1
                
                if input[p] == '.':
                    isFile = True
                
                p += 1
            
            
            if isFile:
                res = max(res, length + table[lvl-1] + lvl - 1)
            else:
                table[lvl] = table[lvl - 1] + length
        
        return res
                
                
                
                
                