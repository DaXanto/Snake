from enum import Enum

GRID_WIDTH = 20        
GRID_HEIGHT = 20       
CELL_SIZE = 20         

INITIAL_SNAKE_LENGTH = 3
MAX_STEPS_WITHOUT_FOOD = 100 * GRID_WIDTH  

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

OPPOSITE_DIRECTION = {
    Direction.UP: Direction.DOWN,
    Direction.DOWN: Direction.UP,
    Direction.LEFT: Direction.RIGHT,
    Direction.RIGHT: Direction.LEFT,
}

class Action(Enum):
    STRAIGHT = 0
    LEFT = 1
    RIGHT = 2

N_ACTIONS = len(Action)


EMPTY = 0
SNAKE_BODY = 1
SNAKE_HEAD = 2
APPLE = 3


REWARD_APPLE = 10.0
REWARD_DEATH = -10.0
REWARD_STEP = -0.01  


FPS = 10
COLOR_BACKGROUND = (0, 0, 0)
COLOR_SNAKE = (0, 255, 0)
COLOR_HEAD = (0, 200, 0)
COLOR_APPLE = (255, 0, 0)
COLOR_GRID_LINE = (40, 40, 40)