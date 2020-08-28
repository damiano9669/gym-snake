class RainbowColors:

    def __init__(self, step=1):
        self.step = step

        self.r = 255
        self.g = 0
        self.b = 0

        self.i = 0

    def set_step_to_fill(self, length):
        self.step = int(765 / length)

    def get_next_color(self):

        if 0 <= self.i < 255:
            self.r -= self.step
            self.b += self.step

        elif 255 <= self.i < 510:
            self.b -= self.step
            self.g += self.step

        elif 510 <= self.i < 765:
            self.g -= self.step
            self.r += self.step

        self.check_max_min()

        self.i += self.step
        if self.i > 765:
            self.i = 0

        return self.r, self.g, self.b

    def check_max_min(self):
        if self.r > 255:
            self.r = 255
        if self.g > 255:
            self.g = 255
        if self.b > 255:
            self.b = 255

        if self.r < 0:
            self.r = 0
        if self.g < 0:
            self.g = 0
        if self.b < 0:
            self.b = 0
