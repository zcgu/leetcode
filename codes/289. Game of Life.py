class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                self.live(board, x, y)
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] /= 10
        
        return
        
    def live(self, board, x, y):
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                x2 = x + i
                y2 = y + j
                
                if x2 >= 0 and x2 < len(board) and y2 >= 0 and y2 < len(board[0]):
                    count += board[x2][y2] % 10
        count -= board[x][y] % 10
        
        if board[x][y] % 10 == 1:
            if count == 2 or count == 3:
                board[x][y] += 10
        else:
            if count == 3:
                board[x][y] += 10