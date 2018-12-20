import sys
import numpy as np
from scipy import signal

DEBUG = False


def main():

    if DEBUG:
        sys.stdin = open("samples/18_input.txt")

    sizes = input().split()
    grid_size = int(sizes[0])
    cookie_size = int(sizes[1])

    grid = np.zeros((grid_size, grid_size))
    for i in range(grid_size):
        grid[i, :] = np.array(input().split(), dtype=np.int)

    max_val = signal.convolve2d(grid, np.ones((cookie_size, cookie_size), dtype=int), mode='valid')
    coords = np.unravel_index(max_val.argmax(), np.shape(max_val))
    print('{} {}'.format(coords[1], coords[0]))


if __name__ == "__main__":
    main()
