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


def gen_sample_results(rounds):
    entries = [f'Entry {x}' for x in range(pow(2, rounds))]
    results = []
    results.append(entries)
    for x in range(rounds):
        latest = [e for idx, e in enumerate(entries) if idx % pow(2,x+1) == 0]
        results.append(latest)
    return results


def get_results():
    import json
    data = json.load(open('../round-5-tournament/songs-by-round.json'))
    return list(data.values())


def gen_bracket(rounds=3, results=[], width=20):

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

        # for line in set(range(n_lines)) - set(row_idxs):
        #     output[line] += ' '*width + '|'

        vals = results[col]
        for row, val in zip(row_idxs, vals):
            just_song = ' - '.join(val.split(" - ")[1:])
            just_song = just_song.split(' (feat')[0]

            for _ in range(col):
                output[row] += ' '*width
            # if is_odd and col != 0:
            #     output[row] += '|'
            # is_odd = not is_odd
            if col != 0:
                # output[row] += '|'
                # padding = width * (col) - len(output[row+1])
                # output[row+1] += ' '*padding + '|'
                if col > 0:
                    for i in range(pow(2,col-1)):
                        line_idx = row - i
                        padding = width * (col) - len(output[line_idx])
                        output[line_idx] += ' '*padding + '|'

                        line_idx = row + 1 + i
                        padding = width * (col) - len(output[line_idx])
                        output[line_idx] += ' '*padding + '|'

                        # output[row-1]
                        # output[row+2]
            output[row] += pad_string(just_song, width)

    for row in output:
        print(row)

# print(coordinates(8))

rounds = 7
width=30
# results = gen_sample_results(rounds)
results = get_results()
gen_bracket(rounds=rounds, results=results, width=30)
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
