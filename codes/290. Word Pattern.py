class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lst = str.split()
        map = {}
        map2 = {}
        
        if len(lst) != len(pattern):
            return False
            
        for i in range(len(pattern)):
            if pattern[i] in map:
                if lst[i] != map[pattern[i]]:
                    return False
            else:
                if lst[i] in map2:
                    return False
                map[pattern[i]] = lst[i]
                map2[lst[i]] = 1
        return True
        