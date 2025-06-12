import glob


def groups():
    return sorted(glob.glob('group-*'))


def results():
    return open('results.txt').read().splitlines()


def group(grp_id):
    return open(grp_id).read().splitlines()


def group_results(g, r):
    return sorted(zip(r,g), key=lambda x: x[0])


def print_pretty_results(gr):
    for r, s in gr:
        print(f'{r}. {s}')
    print()


for idx, grp in enumerate(groups()):
    g = group(grp)
    r = results()[idx]
    gr = group_results(g, r)
    print(grp.upper())
    print_pretty_results(gr)
