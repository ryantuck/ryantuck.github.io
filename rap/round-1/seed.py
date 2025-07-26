import glob


def group_ids():
    return sorted(glob.glob('group-*'))


def rankings():
    lines = open('rankings.txt').read().splitlines()
    assert all(len(line) == 4 for line in lines)
    assert all(set(line) == set('1234') for line in lines)
    return lines


def group(grp_id):
    return open(grp_id).read().splitlines()


def group_results(grp, grp_rankings):
    zipped = sorted(zip(grp_rankings,grp), key=lambda x: x[0])
    return [song for rank,song in zipped]


def results_full():
    output = {}
    for idx, grp in enumerate(group_ids()):
        g = group(grp)
        r = rankings()[idx]
        gr = group_results(g, r)
        output[grp] = gr
    return output


def dump_results():
    import json
    print(json.dumps(results_full()))

dump_results()



def print_pretty_group_results(grp_ranked):
    for rank, song in enumerate(grp_ranked):
        print(f'{rank+1}. {song}')


def print_pretty_all_results():
    for grp_id, songs in results_full().items():
        print(grp_id.upper())
        print_pretty_group_results(songs)
        print()

# print_pretty_all_results()

