class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return True
        if len(preorder) == 1 and preorder[0] == '#':
            return True
        
        l = preorder.split(',')
        i = 1
        while i < len(l):
            if i >= 2 and l[i] == '#' and l[i-1] == '#' and l[i - 2] != '#':
                del l[i]
                del l[i-1]
                l[i-2] = '#'
                i = i-2
            else:
                i += 1
        
        if len(l) == 1 and l[0] == '#':
            return True
        else:
            return False
