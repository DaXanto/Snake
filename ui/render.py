import pygame
from game import constants
from env.snake_env import SnakeEnv
from game.constants import Direction
import random


class Renderer:

    def __init__(self, grid_width=None, grid_height=None, cell_size=None):
        self.grid_width = grid_width or constants.GRID_WIDTH
        self.grid_height = grid_height or constants.GRID_HEIGHT
        self.cell_size = cell_size or constants.CELL_SIZE

        pygame.init()
        pygame.display.set_caption("Snake RL")

        self.screen_width = self.grid_width * self.cell_size
        self.screen_height = self.grid_height * self.cell_size
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 20)

    def render(self, game, fps=None, extra_text=None):
    
        self._handle_events()

        self.screen.fill(constants.COLOR_BACKGROUND)
        self._draw_grid_lines()
        self._draw_apple(game.apple)
        self._draw_snake_body(game.snake_body)
        self._draw_snake_head(game.snake_head)

        if extra_text:
            self._draw_text(extra_text)

        pygame.display.flip()
        self.clock.tick(fps or constants.FPS)

    def _handle_events(self):
        # Permet de fermer proprement la fenêtre (sinon "not responding")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

    def _draw_grid_lines(self):
        for x in range(0, self.screen_width, self.cell_size):
            pygame.draw.line(self.screen, constants.COLOR_GRID_LINE, (x, 0), (x, self.screen_height))
        for y in range(0, self.screen_height, self.cell_size):
            pygame.draw.line(self.screen, constants.COLOR_GRID_LINE, (0, y), (self.screen_width, y))

    def _draw_cell(self, position, color):
        x, y = position
        rect = pygame.Rect(
            x * self.cell_size, y * self.cell_size,
            self.cell_size, self.cell_size
        )
        pygame.draw.rect(self.screen, color, rect)

    def _draw_snake_body(self, snake_body):
        for segment in snake_body:
            self._draw_cell(segment, constants.COLOR_SNAKE)

    def _draw_snake_head(self, snake_head):
        self._draw_cell(snake_head, constants.COLOR_HEAD)

    def _draw_apple(self, apple):
        self._draw_cell(apple, constants.COLOR_APPLE)

    def _draw_text(self, text):
        surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(surface, (5, 5))

    def close(self):
        pygame.quit()


if __name__ == "__main__":

    env = SnakeEnv()
    renderer = Renderer()

    actions = list(Direction)

    while not env.game.died:
        action = random.choice(actions)
        _,_,_,_ = env.step(action)

        renderer.render(env.game, extra_text=f"Score: {len(env.game.snake_body)}")

    renderer.close()