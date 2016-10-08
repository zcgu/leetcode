class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        # 这题挺烦
        # 从左往右走，
        # 1.第一位是0，count必须是0. 
        # 2.第一位是1，count大于0，第二位必须是0 
        # 3.count为0，数开头的1，必须大于1个
        # 4.最后count必须是0
        
        if not data: return False
        
        count = 0
        for p in range(len(data)):
            if data[p] & 0x80 == 0:
                if count != 0:
                    return False
            elif count != 0:
                if data[p] & 0x40 != 0:
                    return False
                count -= 1
            else:
                i = 6
                while i > 0 and data[p] & ( 1 << i) != 0:
                    count += 1
                    i -= 1
                if count == 0:
                    return False
        
        return count == 0
        
