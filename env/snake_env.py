from game.snake_game import SnakeGame
from game import constants

class SnakeEnv:
    def __init__(self):
        self.game = SnakeGame()

    
    def step(self,action : constants.Direction):
        ate_apple,died = self.game.compute_action(action)

        next_state = self.get_state()
        reward = self.get_reward(ate_apple,died)
        done = died

        print(done)
        return next_state,reward,done,{}
    
    def get_state(self):
        return self.game.board
    
    def get_reward(self,ate_apple,died):
        if ate_apple:
            return constants.REWARD_APPLE
        if died:
            return constants.REWARD_DEATH
        return constants.REWARD_STEP

    def reset(self):
        self.game = SnakeGame()

if __name__ == "__main__":
    snake_env = SnakeEnv()
    print(snake_env.get_state())
    snake_env.step(constants.Direction.RIGHT)
    print(snake_env.get_state())