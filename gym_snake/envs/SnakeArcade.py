import random

"""
    Simple snake game class
    
    Modified from: https://gist.github.com/HonzaKral/833ee2b30231c53ec78e
"""


class SnakeArcade:
    ACTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    DIRECTIONS = {
        'NORTH': [-1, 0],
        'EAST': [0, 1],
        'SOUTH': [1, 0],
        'WEST': [0, -1]
    }

    def __init__(self, array_size=20):
        """
            init the game
        :param array_size: size of the grid
        """
        self.array_size = array_size

        init_i = random.randint(0, array_size - 1)
        init_j = random.randint(2, array_size - 1)
        self.snake = random.choice([
            [[init_i, init_j], [init_i, init_j - 1], [init_i, init_j - 2]],
            [[init_j, init_i], [init_j - 1, init_i], [init_j - 2, init_i]]
        ])

        self.place_fruit()

        self.n_points = 0

    def place_fruit(self, coord=None):
        """
            to place a fruit
        :param coord:
        :return:
        """
        if coord:
            self.fruit = coord

        while True:
            row = random.randint(0, self.array_size - 1)
            col = random.randint(0, self.array_size - 1)
            if [row, col] not in self.snake:
                self.fruit = [row, col]
                return

    def step(self, action):
        """
            to move the snake
        :param action:
        :return: (boolean) done
        """
        if action not in self.ACTIONS:
            raise Exception(f'Action {action} is not allowed. Available actions are: {self.ACTIONS}.')

        direction = self.DIRECTIONS[action]

        old_head = self.snake[0]
        new_head = [old_head[0] + direction[0], old_head[1] + direction[1]]

        if (
                new_head[0] < 0 or
                new_head[0] >= self.array_size or
                new_head[1] < 0 or
                new_head[1] >= self.array_size or
                new_head in self.snake
        ):
            return True

        if new_head == self.fruit:
            self.n_points += 1
            self.snake.insert(0, new_head)

            if len(self.snake) == self.array_size ** 2:
                self.fruit = [None, None]
                return True

            self.place_fruit()
        else:
            del self.snake[-1]
            self.snake.insert(0, new_head)

        return False
