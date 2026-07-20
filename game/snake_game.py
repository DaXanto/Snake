from random import randint
from game import constants

class SnakeGame:
    def __init__(self):
        self.grid_height = constants.GRID_HEIGHT
        self.grid_width = constants.GRID_WIDTH
        self.snake_length = constants.INITIAL_SNAKE_LENGTH

        self.died = False
        self.win = False
        self.ate_apple = False
        self.snake_body = []
        self.snake_head = (0,0)
        self.apple = ()

        self.create_snake()
        self.create_apple()
        self.board = self.create_board()


    def create_snake(self):
        self.snake_head = (self.grid_width//2,self.grid_height//2)

        self.snake_body = [(self.grid_width//2 - i,self.grid_height//2)
                           for i in range(1,self.snake_length)]
        
    def create_apple(self):
        possible_apple = [(x,y)for x in range(self.grid_width) for y in range(self.grid_height) if (x,y) not in self.snake_body and (x,y) != self.snake_head]
        random_number = randint(0,len(possible_apple)-1)

        apple_x,apple_y = possible_apple[random_number]
        self.apple = (apple_x,apple_y)


    def compute_action(self,action):
        hx, hy = self.snake_head
        dx, dy = action.value
        new_head = (hx + dx, hy + dy)

        self.died = self.is_dead(new_head)

        if self.died:
            return self.ate_apple, self.died
        
        self.snake_body.insert(0,self.snake_head)
        self.snake_head = new_head
        self.ate_apple = (self.apple == self.snake_head)

        if self.ate_apple:
            self.create_apple()
        else:
            self.snake_body.pop()

        self.board = self.create_board()

        return self.ate_apple,self.died

    def is_dead(self,new_head):
        x,y = new_head
        out_of_bound =  0 > x or x >= self.grid_width or 0 > y or y >= self.grid_height
        self_collision = new_head in self.snake_body
        return out_of_bound or self_collision


    def create_board(self):
        board = [[constants.EMPTY for j in range(self.grid_height)] for i in range(self.grid_width)]
        board[self.snake_head[0]][self.snake_head[1]] = constants.SNAKE_HEAD
        board[self.apple[0]][self.apple[1]] = constants.APPLE
        for point in self.snake_body:
            board[point[0]][point[1]] = constants.SNAKE_BODY
        
        return board
        

if __name__ == "__main__":
    game = SnakeGame()
    print(game.board)
