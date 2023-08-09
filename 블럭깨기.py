#블럭깨기.py
import os
import random
import time

class BlockBreakerGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.paddle_x = width // 2
        self.ball_x = random.randint(1, width - 1)
        self.ball_y = height - 2
        self.ball_dx = 1
        self.ball_dy = -1
        self.bricks = [[True] * width for _ in range(height // 2)]

    def draw(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        for row in self.bricks:
            print(''.join(['#' if brick else ' ' for brick in row]))
        print(' ' * self.paddle_x + '=' + ' ' * (self.width - self.paddle_x - 1))
        print(' ' * self.ball_x + 'O')
        print('=' * self.width)

    def update(self):
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        if self.ball_x == 0 or self.ball_x == self.width - 1:
            self.ball_dx *= -1

        if self.ball_y == 0:
            self.ball_dy *= -1

        if self.ball_y == self.height - 2 and abs(self.ball_x - self.paddle_x) <= 1:
            self.ball_dy *= -1

        if self.ball_y == self.height - 1:
            return False

        if self.bricks[self.ball_y // 2][self.ball_x]:
            self.bricks[self.ball_y // 2][self.ball_x] = False
            self.ball_dy *= -1

        return True

    def run(self):
        while True:
            self.draw()
            if not self.update():
                break
            time.sleep(0.1)

if __name__ == "__main__":
    width = 40
    height = 20
    game = BlockBreakerGame(width, height)
    game.run()
