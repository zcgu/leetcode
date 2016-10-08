class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        lst = []
        
        for d in data:
            lst.append(self.convert(d))
        
        while lst:
            if lst[0][0] == '0':
                del lst[0]
                continue
            if lst[0][0] == '1' and lst[0][1] == '0':
                
                return False
            
            count = 0
            start = -1
            for i, s in enumerate(lst):
                if start != -1:
                    break
                for c in s:
                    if c == '1':
                        count += 1
                    else:
                        start = i
                        break
    
            for i in range(start + 1, start + count):
                if i >= len(lst):
                    
                    return False
                if lst[i][0] != '1' or lst[i][1] != '0':
                    
                    return False
            
            for _ in range(count):
                del lst[0]
            
        return True
        
        
    def convert(self, num):
        res = ''
        
        for _ in range(8):
            res = str(num % 2) + res
            num /= 2
        
        return res
        