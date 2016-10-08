class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if not input:
            return [0]
            
        index = []
        for i in range(len(input)):
            if input[i] == '+' or input[i] == '-' or input[i] == '*':
                index.append(i)
        
        if not index:
            return [int(input)]
        
        res = []
        for i in index:
            res1 = self.diffWaysToCompute(input[:i])
            res2 = self.diffWaysToCompute(input[i + 1:])
            
            for r1 in res1:
                for r2 in res2:
                    if input[i] == '+':
                        res.append(r1 + r2)
                    elif input[i] == '-':
                        res.append(r1 - r2)
                    else:
                        res.append(r1 * r2)
        return res