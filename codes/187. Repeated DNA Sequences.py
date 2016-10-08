class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        table = {}
        
        for i in range(len(s) - 10 + 1):    # interesting
            table[s[i:i+10]] = table[s[i:i+10]] + 1 if s[i:i+10] in table else 1
        
        res = []
        for s, num in table.items():
            if num >= 2:
                res.append(s)
        return res