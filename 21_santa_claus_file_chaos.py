import sys
import math

DEBUG = False


class Compartment(object):
    """ Container for items that keeps a running sum """
    def __init__(self):
        self.files = []
        self.sum = 0

    def append(self, file):
        self.files.append(file)
        self.sum += file

    def __str__(self):
        """ Printable representation """
        return 'Bin(sum={}, items={})'.format(self.sum, self.files)


def pack(files, max_value):
    files = sorted(files, reverse=True)
    compartments = []

    for file in files:
        # Try to fit file into a compartment
        for compartment in compartments:
            if compartment.sum + file <= max_value:
                compartment.append(file)
                break
        else:
            # file didn't fit into any compartment, start a new compartment
            compartment = Compartment()
            compartment.append(file)
            compartments.append(compartment)

    return compartments


def pack_and_print(file_widths, compartment_width, compartments_per_cabinet):
    number_of_compartments = len(pack(file_widths, compartment_width))
    return math.ceil(number_of_compartments / compartments_per_cabinet)


def main():

    if DEBUG:
        sys.stdin = open("samples/21_input.txt")

    compartments_per_cabinet = int(input())
    compartment_width = int(input())
    num_files = int(input())
    if num_files == 0:
        print(0)
    else:
        print(pack_and_print([int(w) for w in input().split(', ')], compartment_width, compartments_per_cabinet))


if __name__ == "__main__":
    main()
