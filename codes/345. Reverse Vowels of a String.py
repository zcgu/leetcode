class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = list(s)

        l = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        p1 = 0
        p2 = len(slist) - 1
        
        while p1 <= p2:
            if slist[p1] not in l:
                p1 += 1
            elif slist[p2] not in l:
                p2 -= 1
            else:
                slist[p1], slist[p2] = slist[p2], slist[p1]
                p1 += 1             # 特别容易忘
                p2 -= 1
        
        return "".join(slist)