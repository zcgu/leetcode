# A string such as "word" contains the following abbreviations:

# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Given a target string and a set of strings in a dictionary, find an abbreviation of this target string with the smallest possible length such that it does not conflict with abbreviations of the strings in the dictionary.

# Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has length = 4.

# Note:
# In the case of multiple answers as shown in the second example below, you may return any one of them.
# Assume length of target string = m, and dictionary size = n. You may assume that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.
# Examples:
# "apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

# "apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").



class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        if not target:
            return ''
            
        dic = [word for word in dictionary if len(word) == len(target)]
        
        # lst = [set() for _ in range(len(target))]
        
        
        # for word in dic:
        #     for i in range(len(word)):
        #         lst[i].add(word[i])
        
        # able = [True for _ in range(len(target))]
        
        # for i in range(len(target)):
        #     if target[i] in lst[i]:
        #         able[i] = False
        
        
        if not dic:
            return str(len(target))
            
            
        

        self.res = list(target)
                    
        self.trie = self.build(dic)
        # print self.find(self.trie, [1, 'e', 5, 'e'])
        for jump in reversed(range(len(target) + 1)):
            self.dfs(target, jump, [])
    
        return ''.join([str(s) for s in self.res])
        
    def dfs(self, target, jumpnum, lst):
        # print lst, target, jumpnum
        if not target:
            if jumpnum == 0:
                if not self.find(self.trie, lst):
                    if len(lst) < len(self.res):
                        self.res = lst
                
                return None
            else:
                return None
        
        self.dfs(target[1:], jumpnum, lst + [target[0]])

        if jumpnum > 0:
            if lst and isinstance(lst[-1], int):
                self.dfs(target[1:], jumpnum - 1, lst[:-1] + [lst[-1] + 1])
                
            else:
                self.dfs(target[1:], jumpnum - 1, lst + [1])

        return None
            
        
        
    def build(self, dic):
        trie = {}
        
        for word in dic:
            t = trie
            
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            
            t['*'] = '*'
        
        return trie
    
    def find(self, t, lst):
        if not lst:
            if '*' in t: return True
            else: return False
            
        if isinstance(lst[0], basestring):
            if lst[0] not in t:
                return False
            else:
                return self.find(t[lst[0]], lst[1:])
        
        else:
            lst[0] -= 1
            lst2 = lst
            if lst[0] == 0:
                lst2 = lst[1:]
                
            for c in t:
                if c != '*' and self.find(t[c], lst2):
                    return True
            
            lst[0] += 1
            return False
            
        
        
