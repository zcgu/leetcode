class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = {}
        
        for s in strs:
            ss = tuple(sorted(s))
            if ss in table:
                table[ss].append(s)
            else:
                table[ss] = [s]
        
        return table.values()