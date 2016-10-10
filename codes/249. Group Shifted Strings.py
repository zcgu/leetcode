# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
# A solution is:

# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        table = {}
        
        for s in strings:
            lst = []
            for i in range(1, len(s)):
                num = ord(s[i]) - ord(s[i - 1])
                if num < 0:
                    num += 26
                lst.append(num)
            t = tuple(lst)
            
            if t in table:
                table[t].append(s)
            else:
                table[t] = [s]
        
        return table.values()
