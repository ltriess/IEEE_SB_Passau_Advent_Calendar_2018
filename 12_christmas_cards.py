import sys
import textwrap

DEBUG = True


num_characters = 38
num_rows = 4

christmas_greetings = ['ein frohes Fest', 'ein schönes Fest', 'frohe Weihnachten', 'erholsame Weihnachten',
                       'ein frohes Weihnachtsfest', 'ein schönes Weihnachtsfest', 'frohe und erholsame Weihnachten',
                       'ein frohes und gesegnetes Weihnachten', 'ein frohes und gesegnetes Weihnachtsfest']
new_years_greetings = ['und ein frohes Neues', 'und einen guten Rutsch', 'und ein erfolgreiches neues Jahr',
                       'und einen guten Rutsch ins neue Jahr', 'und ein erfolgreiches und gesundes neues Jahr']
endings = ['Santa Claus', '']


def calculate_remaining_space(output):
    lines = num_rows - len(output) + 1
    characters = [num_characters] * (lines - 1)
    characters.insert(0, num_characters - len(output[-1]))
    return lines, characters


def check_silvester(output, lines_to_fill, character_space):
    minimal_wrap = textwrap.wrap(
        output[-1] + ' ' + christmas_greetings[0] + ' ' + new_years_greetings[0] + '. ' + endings[0] + '.',
        num_characters
    )
    if len(minimal_wrap) < lines_to_fill:
        return True
    elif len(minimal_wrap) == lines_to_fill:
        if len(minimal_wrap[-1]) > character_space[-1]:
            return False
        else:
            return True
    else:
        return False


def make_title(women, men):
    result = ''

    def append_names(names, result):
        for i, name in enumerate(sorted(names)):
            if i == 0:
                result += ' {}'.format(name)
            elif i == (len(names) - 1):
                result += ' und {}'.format(name)
            else:
                result += ', {}'.format(name)
        return result

    if not len(women) == 0:
        result += 'Liebe'
        result = append_names(women, result)
        if not len(men) == 0:
            result += ', '
    if not len(men) == 0:
        result += 'Lieber'
        result = append_names(men, result)

    return textwrap.wrap(result + ',', num_characters)


def main():

    if DEBUG:
        sys.stdin = open("samples/12_input.txt")

    while True:
        try:
            instructions = input().split(',')
        except:
            return

        women = []
        men = []
        i = 0
        while i < len(instructions):
            if instructions[i] == 'w':
                women.append(instructions[i + 1])
            elif instructions[i] == 'm':
                men.append(instructions[i + 1])
            else:
                raise ValueError
            i += 2

        single = len(men) + len(women) == 1
        endings[1] = 'Dein Weihnachtsmann' if single else 'Euer Weihnachtsmann'

        output = []
        output += make_title(women, men)
        if single:
            wishes = textwrap.wrap(output[-1] + ' ich wünsche Dir', num_characters)
        else:
            wishes = textwrap.wrap(output[-1] + ' ich wünsche euch', num_characters)
        output = output[:-1]
        output += wishes

        lines_to_fill, character_space = calculate_remaining_space(output)

        if check_silvester(output, lines_to_fill, character_space):
            combination = (None, None, None)
            minval = num_characters
            for i, christmas_greeting in enumerate(christmas_greetings):
                for j, ending in enumerate(endings):
                    wrap = textwrap.wrap(
                        output[-1] + ' ' + christmas_greeting + ' ' + new_years_greetings[0] + '. ' + ending + '.',
                        num_characters
                    )
                    if len(wrap) > lines_to_fill:
                        continue
                    if num_characters - len(wrap[-1]) < minval:
                        minval = num_characters - len(wrap[-1])
                        combination = (i, 0, j)
            minval = num_characters
            for h, new_years_greeting in enumerate(new_years_greetings):
                wrap = textwrap.wrap(
                        output[-1] + ' ' + christmas_greetings[combination[0]] + ' ' + new_years_greeting + '. ' + endings[combination[2]] + '.',
                        num_characters
                    )
                if len(wrap) > lines_to_fill:
                    continue
                if num_characters - len(wrap[-1]) < minval:
                    minval = num_characters - len(wrap)
                    combination = (combination[0], h, combination[2])

            greetings = textwrap.wrap(
                output[-1] + ' ' + christmas_greetings[combination[0]] + ' ' + new_years_greetings[combination[1]]
                + '. ' + endings[combination[2]] + '.',
                num_characters
            )
            output = output[:-1]
            output += greetings
        else:
            combination = (None, None)
            minval = num_characters
            for i, christmas_greeting in enumerate(christmas_greetings):
                for j, ending in enumerate(endings):
                    wrap = textwrap.wrap(output[-1] + ' ' + christmas_greeting + '. ' + ending + '.',
                                         num_characters)
                    if len(wrap) > lines_to_fill:
                        continue
                    if num_characters - len(wrap[-1]) < minval:
                        minval = num_characters - len(wrap[-1])
                        combination = (i, j)

            greetings = textwrap.wrap(output[-1] + ' ' + christmas_greetings[combination[0]] + '. ' + endings[combination[1]] + '.', num_characters)
            output = output[:-1]
            output += greetings

        out_str = ''
        for line in output:
            out_str += line + '|'
        print(out_str[:-1])


if __name__ == "__main__":
    main()
