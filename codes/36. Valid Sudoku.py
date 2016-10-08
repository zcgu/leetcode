class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for x in range(9):
            lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            
            for y in range(9):
                if board[x][y] == '.':
                    pass
                elif board[x][y] in lst:
                    del lst[lst.index(board[x][y])]
                else:
                    # print 1, x, y
                    return False
        
        for y in range(9):
            lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            
            for x in range(9):
                if board[x][y] == '.':
                    pass
                elif board[x][y] in lst:
                    del lst[lst.index(board[x][y])]
                else:
                    # print 2, x, y
                    return False
        
        for n in [0, 3, 6]:
            for m in [0, 3, 6]:
                lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                for x in range(3):
                    for y in range(3):
                        if board[n+x][m+y] == '.':
                            pass
                        elif board[n+x][m+y] in lst:
                            del lst[lst.index(board[n+x][m+y])]
                        else:
                            # print 3, n+x, m+y
                            return False
        
        return True