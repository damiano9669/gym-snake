import gym
from gym import spaces

from gym_snake.envs.Graphic import Graphic
from gym_snake.envs.SnakeArcade import SnakeArcade


class SnakeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    fruit_color = (241, 196, 15)
    background_color = (0, 0, 0)

    def __init__(self, array_size=10, scale_factor=50):
        self.array_size = array_size
        self.scale_factor = scale_factor

        self.snake = SnakeArcade(self.array_size)
        self.g = Graphic(self.array_size, self.fruit_color, self.background_color, scale=self.scale_factor)

        self.action_space = spaces.Discrete(len(self.snake.ACTIONS))
        self.observation_space = self.g.draw(self.snake).shape

    def step(self, action):
        done = self.snake.step(action)
        observation = self.g.draw(self.snake)
        return observation, self.snake.n_points, done, {}

    def reset(self):
        self.snake = SnakeArcade(self.array_size)
        observation = self.g.draw(self.snake)
        return observation

    def render(self, mode='human'):
        observation = self.g.draw(self.snake)
        return observation

    def close(self):
        self.g.close()
