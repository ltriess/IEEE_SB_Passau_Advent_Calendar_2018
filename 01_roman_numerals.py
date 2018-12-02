value_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_decimal(rn_str):
    result = 0
    i = 0

    while i < len(rn_str):
        p1 = value_map[rn_str[i]]

        if i + 1 < len(rn_str):
            p2 = value_map[rn_str[i+1]]
            if p1 >= p2:
                result += p1
                i += 1
            else:
                result += p2 - p1
                i += 2
        else:
            result += p1
            i += 1

    return result


def main():
    for _ in range(int(input())):
        print('{}'.format(roman_to_decimal(input())))


if __name__ == "__main__":
    main()
