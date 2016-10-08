class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        m = len(board)
        n = len(board[0])
        
        for x in range(len(board)):
            self.mark(board, x, 0)
            self.mark(board, x, n - 1)
            
        for y in range(n):
            self.mark(board, 0, y)
            self.mark(board, m-1, y)
        
        for x in range(m):
            for y in range(n):
                if board[x][y] != '1':
                    board[x][y] = 'X'
                else:
                    board[x][y] = 'O'
                    
            
    def mark(self, b, x1, y1):
        
        que = [(x1, y1)]
        
        while que:
            x, y = que.pop()
            
            if x < 0 or x >= len(b) or y < 0 or y >= len(b[0]) or b[x][y] != 'O':
                continue

            b[x][y] = '1'
            
            for xx, yy in [(x+1, y), (x-1,y), (x,y+1), (x, y-1)]:
                que.append((xx, yy))