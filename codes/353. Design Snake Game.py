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
        self.m = m  = height
        self.n = n = width
        self.table = {(0, 0) : 1}
        self.size = 0
        self.x = 0
        self.y = 0
        self.tx = 0
        self.ty = 0
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

        x, y, table, tx, ty = self.x, self.y, self.table, self.tx, self.ty
        
        if direction == 'U': xx, yy = x -1, y
        elif direction == 'D': xx, yy = x + 1, y
        elif direction == 'L': xx, yy = x, y - 1
        else: xx, yy = x, y + 1
        
        if xx < 0 or yy < 0 or xx >= self.m or yy >= self.n: return -1
        
        if self.food and [xx, yy] == self.food[0]:
            self.size += 1
            self.food = self.food[1:]
            table[(xx, yy)] = table[(x, y)] + 1
            self.x, self.y = xx, yy
            return self.size
        else:
            if (xx != tx or yy != ty) and (xx, yy) in table and table[(xx, yy)] != 0:
                return -1
            
            tail = table[(tx, ty)]
            
            table[(xx,yy)] = table[(x, y)] + 1
            self.x, self.y = xx, yy
            for i, j in [(1,0), (-1,0), (0,1), (0, -1)]:
                if self.m >tx + i >=0 and self.n > ty + j >= 0 and (tx +i, ty+j) in table and  table[(tx + i, ty + j)] == tail + 1:
                    if xx != tx or yy != ty:  table[(tx, ty)] = 0
                    self.tx, self.ty = tx + i, ty + j
                    return self.size

        

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)






