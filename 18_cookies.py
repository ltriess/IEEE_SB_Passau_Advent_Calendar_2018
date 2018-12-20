import sys

DEBUG = True


def main():

    if DEBUG:
        sys.stdin = open("samples/18_input_01.txt")

    sizes = input().split()
    grid_size = int(sizes[0])
    cookie_size = int(sizes[1])

    grid = []
    for i in range(grid_size):
        grid.append([int(i) for i in input().split()])

    out_size = grid_size - cookie_size + 1
    sums = [[None]*out_size for _ in range(out_size)]
    for i in range(out_size):
        for j in range(out_size):
            sums[i][j] = sum(sum([m[j:(j + cookie_size)] for m in grid[i:(i + cookie_size)]], []))

    coords = [[y, x] for x, m in enumerate(sums) for y, val in enumerate(m) if val == max(max(sums))][0]
    print('{} {}'.format(coords[0], coords[1]))


if __name__ == "__main__":
    main()
