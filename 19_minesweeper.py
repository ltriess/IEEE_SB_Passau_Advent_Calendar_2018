import sys

DEBUG = True


def coords_2D_to_1D(row, column, width):
    return row * width + column


def coords_1D_to_2D(index, width):
    return index // width, index % width


def main():

    if DEBUG:
        sys.stdin = open("samples/19_input.txt")

    line = input().split()
    width = int(line[0])
    height = int(line[1])

    board = []
    for _ in range(height):
        board.extend(list(input()))

    for idx, element in enumerate(board):
        if element == '*':
            continue
        else:
            if element == '.':
                element = 0
            mines_count = 0

            r, c = coords_1D_to_2D(idx, width)
            for i in [r - 1, r, r + 1]:
                if i < 0 or i > (height - 1):
                    continue
                for j in [c - 1, c, c + 1]:
                    if j < 0 or j > (width - 1):
                        continue
                    if board[coords_2D_to_1D(i, j, width)] == '*':
                        mines_count += 1

            if not int(element) == mines_count:
                print('Nein')
                exit()

    print('Ja')


if __name__ == "__main__":
    main()
