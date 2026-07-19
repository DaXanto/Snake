from random import randint
class SnakeGame:
    def __init__(self,heigth,width,snake_length):
        self.heigth = heigth
        self.width = width
        self.snake_length = snake_length

        self.snake_head = (0,0)

        self.board = [[0 for j in range(self.heigth)] for i in range(self.width)]

        self.create_game()

    

    def create_game(self):
        self.create_snake()

        self.create_apple()


    def create_snake(self):
        self.board[self.width//2][self.heigth//2] = 1

        for i in range(1,self.snake_length):
            self.board[self.width//2 - i][self.heigth//2] = 2
        
    def create_apple(self):
        possible_apple = [(x,y)for x in range(len(self.board)) for y in range(len(self.board[x])) if self.board[x][y] == 0]
        random_number = randint(0,len(possible_apple)-1)

        apple_x,apple_y = possible_apple[random_number]

        self.board[apple_x][apple_y] = 3


    def get_state(self):
        return self.board 


if __name__ == "__main__":
    game = Game(20,20,3)
    print(game.board)
