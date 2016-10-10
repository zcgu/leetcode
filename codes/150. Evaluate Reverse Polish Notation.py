class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens: return 0
        
        p = 0
        while len(tokens) > 1:
            
            while tokens[p] not in ['+', '-', '*', '/']:
                p += 1
            
            num1 = int(tokens.pop(p - 2))
            num2 = int(tokens.pop(p - 2))
            sign = tokens.pop(p - 2)
            
            if sign == '+':
                res = num1 + num2
            elif sign == '-':
                res = num1 - num2
            elif sign == '*':
                res = num1 * num2
            else:
                if num1 * num2 < 0 and num1 % num2 != 0:
                    res = num1 / num2 + 1
                else:
                    res = num1 / num2
            
            tokens.insert(p - 2, res)
            p = p - 2
        
        return int(tokens[0])
