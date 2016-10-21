# Design a Tic-tac-toe game that is played between two players on a n x n grid.

# You may assume the following rules:

# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves is allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
# Example:
# Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

# TicTacToe toe = new TicTacToe(3);

# toe.move(0, 0, 1); -> Returns 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |

# toe.move(0, 2, 2); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |

# toe.move(2, 2, 1); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|

# toe.move(1, 1, 2); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|

# toe.move(2, 0, 1); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|

# toe.move(1, 0, 2); -> Returns 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|

# toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|
# Follow up:
# Could you do better than O(n2) per move() operation?

# Hint:

# Could you trade extra space such that move() operation can be done in O(1)?
# You need two arrays: int rows[n], int cols[n], plus two variables: diagonal, anti_diagonal.
# Show Company Tags
# Show Tags

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rows = [0 for _ in range(n)]
        self.cols = [0 for _ in range(n)]
        self.d1 = self.d2 = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        num = 1 if player == 2 else - 1
        
        self.rows[row] += num
        self.cols[col] += num
        
        if row == col: self.d1 += num
        if row == self.n - col - 1: self.d2 += num
        
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or \
            abs(self.d1) == self.n or abs(self.d2) == self.n:
                return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)



# class TicTacToe(object):

#     def __init__(self, n):
#         """
#         Initialize your data structure here.
#         :type n: int
#         """
#         self.m = [[0 for _ in range(n)] for _ in range(n)]

#     def move(self, row, col, player):
#         """
#         Player {player} makes a move at ({row}, {col}).
#         @param row The row of the board.
#         @param col The column of the board.
#         @param player The player, can be either 1 or 2.
#         @return The current winning condition, can be either:
#                 0: No one wins.
#                 1: Player 1 wins.
#                 2: Player 2 wins.
#         :type row: int
#         :type col: int
#         :type player: int
#         :rtype: int
#         """
#         n = len(self.m)
        
#         self.m[row][col] = player

#         if all(self.m[x][col] == player for x in range(n)):
#             return player

#         if all(self.m[row][y] == player for y in range(n)):
#             return player

#         if all(self.m[i][i] == player for i in range(n)):
#             return player

#         if all(self.m[n - 1 - i][i] == player for i in range(n)):
#             return player
#         return 0


# # Your TicTacToe object will be instantiated and called as such:
# # obj = TicTacToe(n)
# # param_1 = obj.move(row,col,player)

