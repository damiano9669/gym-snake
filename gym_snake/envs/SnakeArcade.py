import random

"""
    Simple snake game class
    
    from: https://gist.github.com/HonzaKral/833ee2b30231c53ec78e
"""


class SnakeArcade:
    DIRS = ['NONE', 'UP', 'RIGHT', 'DOWN', 'LEFT']

    DIRECTIONS = {
        'NONE': [0, 0],
        'UP': [-1, 0],
        'RIGHT': [0, 1],
        'DOWN': [1, 0],
        'LEFT': [0, -1]
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
            [[init_j, init_i], [init_j - 1, init_i], [init_j - 2, init_i]]])

        self.place_fruit()

        self.n_fruits = 0
        self.last_action = 0

    def place_fruit(self, coord=None):
        """
            to place a fruit
        :param coord:
        :return:
        """
        if coord:
            self.fruit = coord
            return

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
        :return:
        """
        if action == 0:
            action = self.last_action
        else:
            self.last_action = action

        keyword = self.DIRS[action]
        movement = self.DIRECTIONS[keyword]

        old_head = self.snake[0]
        new_head = [old_head[0] + movement[0], old_head[1] + movement[1]]

        if (
                new_head[0] < 0 or
                new_head[0] >= self.array_size or
                new_head[1] < 0 or
                new_head[1] >= self.array_size or
                new_head in self.snake

        ):
            return False

        if new_head == self.fruit:
            self.n_fruits += 1
            self.snake.insert(0, new_head)

            if len(self.snake) == self.array_size ** 2:
                self.fruit = [None, None]
                return True

            self.place_fruit()
        else:
            del self.snake[-1]
            self.snake.insert(0, new_head)

        return True
