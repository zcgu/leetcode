# Given an 2D board, count how many different battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column).
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.
# Your algorithm should not modify the value of the board.

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        res = 0        
        ships = set()

        m = len(board)
        n = len(board[0])

        for x in range(m):
            for y in range(n):
                if board[x][y] == 'X':
                    visited = False
                    for xx, yy in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                        if (xx, yy) in ships:
                            visited = True
                            break
                    if not visited:
                        res += 1
                    ships.add((x, y))
        return res

