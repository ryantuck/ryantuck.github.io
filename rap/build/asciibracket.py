def pad_string(s, width, pad_char='_', left_padding=2):
    padding_1 = pad_char * left_padding
    padding_str = pad_char * (width-len(s)-left_padding-2)
    return f'{padding_1} {s} {padding_str}'



def bracket(a, b, width, height, a_wins=None):
    print(pad_string(a, width))
    for _ in range(height):
        print(' '*width + '|')
    print(' '*width + '|' + pad_string(a, width))
    for _ in range(height):
        print(' '*width + '|')
    print(pad_string(b, width) + '|')


def coordinates(depth):

    n0 = pow(2, depth - 1)      # original entries
    n_lines = n0 * 2            # fn(n0, height)
    mid_line = int(n_lines / 2) # starting point

    output = []
    output.append([mid_line])

    for d in range(depth-1):

        delta = pow(2, depth-2-d)
        last_entry = output[-1]

        new_entry = []
        for x in last_entry:
            new_entry.append(x - delta)
            new_entry.append(x + delta)

        output.append(new_entry)

    return list(reversed(output))


def gen_bracket(rounds=3, width=20):

    n_songs = pow(2, rounds)
    n_lines = n_songs * 2

    indices = coordinates(rounds+1)

    # indices = [
    #     [1,3,5,7,9,11,13,15],
    #     [2,6,10,14],
    #     [4,12],
    #     [8],
    # ]


    output = ['']*n_lines

    for col, row_idxs in enumerate(indices):
        for row in row_idxs:
            for _ in range(col):
                output[row] += ' '*width
            output[row] += pad_string(f'SONG {row}', width)

    for row in output:
        print(row)

# print(coordinates(8))

gen_bracket(rounds=7)
# gen_bracket()
# gen_bracket()
# gen_bracket()


# bracket('Soldier - Eminem', "Ludacris - What's Your Fantasy?", 40, 0, True)
# print()
# bracket('Soldier - Eminem', "Ludacris - What's Your Fantasy?", 40, 0, True)
# print()
# bracket('Soldier - Eminem', "Ludacris - What's Your Fantasy?", 40, 0, True)
# print()
# bracket('Soldier - Eminem', "Ludacris - What's Your Fantasy?", 40, 0, True)



# print(pad_string('Role Model'))
# print(pad_string('Still Fly'))
