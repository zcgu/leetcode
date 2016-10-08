class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 负数的二进制，先将负数变成a = -a - 1,然后用二进制的每一位变一下（可以用15减去每一位，也可以直接xor全1）。
        
        
        # 负数操作
        sign = -1 if num < 0 else 1
        if num < 0:
            num = - num - 1
        
        lst = [0 for _ in range(8)]
        
        i = 7
        while num != 0:
            lst[i] = num % 16
            num /= 16
            i -= 1
        
        # 负数操作
        if sign == -1:
            for i in range(8):
                lst[i] = 15 - lst[i]
        
        for i, num in enumerate(lst):
            if num <= 9:
                lst[i] = str(num)
            else:
                lst[i] = chr(ord('a') + num - 10)
        
        res = ''.join(lst)
        res = res.lstrip('0')
        return res if res else '0'
