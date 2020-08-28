import gym
import matplotlib.pyplot as plt
from gym import spaces

from gym_snake.envs.Graphic import Graphic
from gym_snake.envs.SnakeArcade import SnakeArcade


class SnakeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    array_size = 10

    fruit_color = (241, 196, 15)
    background_color = (0, 0, 0)

    def __init__(self):
        self.snake = SnakeArcade(self.array_size)
        self.g = Graphic(self.array_size, self.fruit_color, self.background_color)

        self.action_space = spaces.Discrete(len(self.snake.DIRS))
        self.observation_space = self.g.draw(self.snake)

    def step(self, action):
        done = not self.snake.step(action)
        observation = self.g.draw(self.snake)
        return observation, self.snake.n_fruits, done, {}

    def reset(self):
        self.snake = SnakeArcade(self.array_size)
        observation = self.g.draw(self.snake)
        return observation

    def render(self, mode='human'):
        observation = self.g.draw(self.snake)
        return observation

    def close(self):
        self.g.close()
