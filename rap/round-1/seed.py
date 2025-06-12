import glob


def groups():
    return sorted(glob.glob('group-*'))


def results():
    return open('results.txt').read().splitlines()


def group(grp_id):
    return open(grp_id).read().splitlines()


def group_results(group, rankings):
    zipped = sorted(zip(rankings,group), key=lambda x: x[0])
    return [s for r,s in zipped]


def results_full():
    output = {}
    for idx, grp in enumerate(groups()):
        g = group(grp)
        r = results()[idx]
        gr = group_results(g, r)
        output[grp] = gr
    return output


def print_pretty_group_results(gr):
    for rank, song in enumerate(gr):
        print(f'{rank+1}. {song}')


def print_pretty_all_results():
    for grp_id, songs in results_full().items():
        print(grp_id.upper())
        print_pretty_group_results(songs)
        print()


print_pretty_all_results()
