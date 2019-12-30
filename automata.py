import argparse
from random import random

from PIL import Image, ImageColor


class Map:

    def __init__(self, width, height):
        self.chance = args.chance
        self.death_limit = args.death
        self.birth_limit = args.birth
        self.cells = [[0 if (random() > self.chance) else 1 for _ in range(width)] for _ in range(height)]

    def make_step(self):
        newmap = [[y for y in x] for x in self.cells]
        for x in range(len(self.cells)):
            for y in range(len(self.cells[0])):
                neighbours = self.count_neighbours(x, y)
                if self.cells[x][y]:
                    if neighbours < self.death_limit:
                        newmap[x][y] = 0
                else:
                    if neighbours > self.birth_limit:
                        newmap[x][y] = 1
        self.cells = newmap

    def count_neighbours(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                n_x = x + i
                n_y = y + j
                if not i and not j:
                    continue
                elif n_x < 0 or n_y < 0 or n_x >= len(self.cells) or n_y >= len(self.cells[0]):
                    count += 1
                elif self.cells[n_x][n_y]:
                    count += 1
        return count

    def draw(self):
        canvas = Image.new("RGB", (args.width, args.height), "white")
        for x in range(len(self.cells)):
            for y in range(len(self.cells[x])):
                if self.cells[x][y]:
                    canvas.putpixel((x, y), ImageColor.getcolor("white", "1"))
                else:
                    canvas.putpixel((x, y), ImageColor.getcolor("black", "1"))
        canvas.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=64)
    parser.add_argument("--height", type=int, default=64)
    parser.add_argument("--birth", type=int, default=4)
    parser.add_argument("--death", type=int, default=3)
    parser.add_argument("--chance", type=int, default=45)
    parser.add_argument("--steps", type=int, default=3)
    args = parser.parse_args()
    args.chance = args.chance / 100
    cell_map = Map(args.width, args.height)
    for _ in range(args.steps):
        cell_map.make_step()
    cell_map.draw()
