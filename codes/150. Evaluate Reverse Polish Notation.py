class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
            
        p = 0
        while len(tokens) > 1:
            while tokens[p] != '+' and tokens[p] != '-' and tokens[p] != '*' and tokens[p] != '/':
                    p += 1
            
            a = int(tokens[p-2])
            b = int(tokens[p-1])
            s = tokens[p]
            
            if s == '+':
                a += b
            elif s == '-':
                a -= b
            elif s == '*':
                a *= b
            else:
                a = a / b + 1 if a % b != 0 and a / b < 0 else a / b        # This is interesting in python
            
            tokens[p-2] = str(a)
            del tokens[p]
            del tokens[p-1]
            p = p - 2
            
            
        return int(tokens[0])