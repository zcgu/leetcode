class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        lst = path.strip('/').split('/')
        lst = [n for n in lst if n != '' and n != '.']

        i = 0
        while i < len(lst):
            if lst[i] == '..':
                del lst[i]
                if i > 0:
                    del lst[i-1]
                    i -= 1
            else:
                i += 1
        
        return '/' + '/'.join(lst)