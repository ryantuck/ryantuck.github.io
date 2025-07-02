def pad_string(s, width, pad_char='_', left_padding=2):
    """
    Example:
        '__ Shook Ones, Pt. II __________________'
    """
    padding_1 = pad_char * left_padding
    padding_str = pad_char * (width-len(s)-left_padding-2)
    return f'{padding_1} {s} {padding_str}'


def coordinates(depth):
    """
    Method: start from midpoint of total lines, get midpoint of above and below, repeat to end.
    Example 8-entry, 3-round bracket:
        indices = [
            [1,3,5,7,9,11,13,15],
            [2,6,10,14],
            [4,12],
            [8],
        ]
    """
    n0 = pow(2, depth - 1)      # original entries
    n_lines = n0 * 2            # fn(n0, h=1)
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


def _tidy_song(song):
    just_song = song.split(" - ")[1:][0]
    just_song = just_song.split('feat')[0]
    just_song = just_song.split('(')[0]
    just_song = just_song.strip()
    return just_song


def get_results():
    import json
    data = json.load(open('../round-5-tournament/songs-by-round.json'))
    return [
        [_tidy_song(s) for s in songs]
        for songs in data.values()
    ]


def gen_bracket(results, width=30):
    rounds = len(results)-1
    n_songs = pow(2, rounds)
    n_lines = n_songs * 2

    indices = coordinates(rounds+1)

    output = ['']*n_lines

    # iterate through all coordinates and place entries accordingly
    for col, row_idxs in enumerate(indices):
        vals = results[col]

        # zip together locations and entries that should populate those slots
        for row, val in zip(row_idxs, vals):

            # pad row n cols worth
            for _ in range(col):
                output[row] += ' '*width

            # add vertical bars to brackets, padding where needed
            if col != 0:
                for i in range(pow(2,col-1)):
                    # above
                    line_idx = row - i
                    padding = width * (col) - len(output[line_idx])
                    output[line_idx] += ' '*padding + '|'
                    # and below
                    line_idx = row + 1 + i
                    padding = width * (col) - len(output[line_idx])
                    output[line_idx] += ' '*padding + '|'

            # finally, write the row for the entry
            output[row] += pad_string(val, width-1 if col>0 else width)

    # return one big text string for later printing
    return '\n'.join(output)


def main():
    import sys
    import json
    width = 40
    results = json.loads(''.join(line for line in sys.stdin))
    output = gen_bracket(results=results, width=width)
    print(output)


main()
