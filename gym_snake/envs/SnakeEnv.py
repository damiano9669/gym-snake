import gym
from gym import spaces

from gym_snake.envs.Graphic import Graphic
from gym_snake.envs.SnakeArcade import SnakeArcade


class SnakeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    fruit_color = (241, 196, 15)
    background_color = (0, 0, 0)

    def __init__(self, array_size=10, render_scale_factor=50):
        self.array_size = array_size
        self.scale_factor = render_scale_factor

        self.snake = SnakeArcade(self.array_size)
        self.g = None

        self.action_space = spaces.Discrete(len(self.snake.ACTIONS))

    def step(self, action):
        done = self.snake.step(action)
        observation = self.get_dictionary()
        return observation, self.snake.n_points, done, {}

    def reset(self):
        self.snake = SnakeArcade(self.array_size)
        return self.get_dictionary()

    def render(self, mode='human'):
        if self.g is None:
            self.g = Graphic(self.array_size, self.fruit_color, self.background_color, scale=self.scale_factor)
        self.g.draw(self.snake)

    def close(self):
        self.g.close()

    def get_dictionary(self):
        return {'snake': self.snake.snake, 'fruit': self.snake.fruit}

    def get_available_actions(self):
        return self.snake.ACTIONS
