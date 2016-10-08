class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # 这题重点不是去0，直接int() 就好，重点是循环。
        
        l1 = version1.split('.')
        l2 = version2.split('.')
        
        while int(l1[-1]) == 0 and len(l1) > 1:
            del l1[-1]
        
        while int(l2[-1]) == 0 and len(l2) > 1:
            del l2[-1]
        
        for i in range(max(len(l1), len(l2))):
            if i >= len(l1):
                return -1
            
            if i >= len(l2):
                return 1
            
            if int(l1[i]) > int(l2[i]):
                return 1
            elif int(l1[i]) < int(l2[i]):
                return -1
        
        return 0