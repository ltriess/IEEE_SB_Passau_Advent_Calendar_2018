import sys

DEBUG = True


def coords_2D_to_1D(row, column, width):
    return row * width + column


def coords_1D_to_2D(index, width):
    return index // width, index % width


def compute_deviation(current_cookie, grid, cookie_size):
    curent_sum = 0
    for j in range(cookie_size ** 2):
        cookie_r, cookie_c = coords_1D_to_2D(j, cookie_size)
        curent_sum += grid[current_cookie[0] + cookie_r][current_cookie[1] + cookie_c]

    return curent_sum / (cookie_size ** 2)


def compute_variance(current_cookie, deviation, grid, cookie_size):
    variance = 0
    for j in range(cookie_size ** 2):
        cookie_r, cookie_c = coords_1D_to_2D(j, cookie_size)
        variance += abs(grid[current_cookie[0] + cookie_r][current_cookie[1] + cookie_c] - deviation) ** 2

    return variance / (cookie_size ** 2)


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
    sums = []
    for i in range(out_size ** 2):
        deviation = compute_deviation(coords_1D_to_2D(i, out_size), grid, cookie_size)
        variance = compute_variance(coords_1D_to_2D(i, out_size), deviation, grid, cookie_size)
        sums.append(deviation - variance)

    coords = coords_1D_to_2D(sums.index(max(sums)), out_size)
    print('{} {}'.format(coords[1], coords[0]))



if __name__ == "__main__":
    main()
