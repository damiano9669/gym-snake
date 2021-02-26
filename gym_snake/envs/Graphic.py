from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

from gym_snake.envs.RainbowColors import RainbowColors


class Graphic:

    def __init__(self, array_size, fruit_color, background_color, scale=20):

        self.array_size = array_size
        self.background_color = background_color
        self.scale = scale

        size = self.array_size * self.scale

        pygame.init()

        self.screen = pygame.display.set_mode((size, size), pygame.NOFRAME)

        self.fruit_surface = pygame.Surface((self.scale, self.scale))
        self.fruit_surface.fill(fruit_color)

        self.snake_surfaces = []
        max_snake_length = self.array_size ** 2
        rainbow = RainbowColors(15)
        # rainbow.set_step_to_fill(max_snake_length)

        for i in range(max_snake_length):
            snk_i = pygame.Surface((self.scale, self.scale))
            color = rainbow.get_next_color()
            snk_i.fill(color)
            self.snake_surfaces.append(snk_i)

        self.font = pygame.font.SysFont("monospace", 15)

        # pygame.time.set_timer(1, self.speed)

    def draw(self, snake_arcade):
        """
        :param snake_arcade: (snake_arcade object)
        :return:
        """

        self.screen.fill(self.background_color)

        for surface, bit in zip(self.snake_surfaces[:len(snake_arcade.snake)], snake_arcade.snake):
            self.screen.blit(surface, (bit[0] * self.scale,
                                       bit[1] * self.scale))

        if snake_arcade.fruit != [None, None]:
            self.screen.blit(self.fruit_surface,
                             (snake_arcade.fruit[0] * self.scale,
                              snake_arcade.fruit[1] * self.scale))

        pygame.display.flip()
        return pygame.surfarray.array3d(self.screen)

    def close(self):
        pygame.quit()
