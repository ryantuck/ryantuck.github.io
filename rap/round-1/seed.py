import glob


def group_ids():
    return sorted(glob.glob('group-*'))


def rankings():
    return open('results.txt').read().splitlines()


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


def print_pretty_group_results(grp_ranked):
    for rank, song in enumerate(grp_ranked):
        print(f'{rank+1}. {song}')


def print_pretty_all_results():
    for grp_id, songs in results_full().items():
        print(grp_id.upper())
        print_pretty_group_results(songs)
        print()


print_pretty_all_results()
