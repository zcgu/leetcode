class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.lst = []
        board = [-1 for i in range(n)]
        self.nextlvl(board, 0, n)
        
        # output
        self.res = []
        for l in self.lst:
            r = ['.' * n for i in range(n)]
            for i in range(n):
                r[i] = r[i][:l[i]] + 'Q' + r[i][l[i]+1:]
            self.res.append(r)
        
        return self.res
            
    def nextlvl(self, board, l, n):
        if l == n:
            self.lst.append(board[:])
            return
        
        for i in range(n):
            board[l] = i
            flag = True
            
            for j in range(l):
                if board[j] == board[l] or abs(board[j] - board[l]) == l - j:
                    flag = False
                    break
            
            if flag:
                self.nextlvl(board, l + 1, n)
                