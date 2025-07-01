box_width = 60


def pad_string(s, width, left_padding=2):
    padding_1 = '_' * left_padding
    padding_str = '_' * (width-len(s)-left_padding-2)
    return f'{padding_1} {s} {padding_str}'



def bracket(a, b, width, height, a_wins=None):
    print(pad_string(a, width))
    for _ in range(height):
        print(' '*width + '|')
    print(' '*width + '|' + pad_string(a, width))
    for _ in range(height):
        print(' '*width + '|')
    print(pad_string(b, width) + '|')


bracket('Soldier - Eminem', "Ludacris - What's Your Fantasy?", 40, 0, True)



# print(pad_string('Role Model'))
# print(pad_string('Still Fly'))
