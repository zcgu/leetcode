# Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

# The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

# You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

# Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

# When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

# Example:
# Given width = 3, height = 2, and food = [[1,2],[0,1]].

# Snake snake = new Snake(width, height, food);

# Initially the snake appears at position (0,0) and the food at (1,2).

# |S| | |
# | | |F|

# snake.move("R"); -> Returns 0

# | |S| |
# | | |F|

# snake.move("D"); -> Returns 0

# | | | |
# | |S|F|

# snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

# | |F| |
# | |S|S|

# snake.move("U"); -> Returns 1

# | |F|S|
# | | |S|

# snake.move("L"); -> Returns 2 (Snake eats the second food)

# | |S|S|
# | | |S|

# snake.move("U"); -> Returns -1 (Game over because snake collides with border)

# Credits:
# Special thanks to @elmirap for adding this problem and creating all test cases.

# Show Company Tags
# Show Tags


class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.lst = [(0, 0)]
        self.m, self.n = height, width
        self.food = food
        
        
    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        m, n, food, lst = self.m, self.n, self.food, self.lst
        
        x, y = self.lst[-1]
        
        if direction == 'U': xx, yy = x - 1, y
        elif direction == 'D': xx, yy = x + 1, y
        elif direction == 'L': xx, yy = x, y - 1
        else: xx, yy = x, y + 1
        
        if xx < 0 or xx >= m or yy < 0 or yy >= n: return -1
        
        if food and [xx, yy] == food[0]:
            lst.append((xx, yy))
            del food[0]
            return len(lst) - 1
        else:
            del lst[0]
            if (xx, yy) in lst: return -1
            lst.append((xx, yy))
            return len(lst) - 1
        
        

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
  

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)






