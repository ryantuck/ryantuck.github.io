

groups = ['000', '001', '002', '003']


def results():
    return open('results.txt').read().splitlines()


def group(x):
    return open(f'group-{x}').read().splitlines()


def group_results(g, r):
    return sorted(zip(r,g), key=lambda x: x[0])


def pretty_results(gr):
    for r, s in gr:
        print(f'{r}. {s}')


for idx, grp in enumerate(groups):
    g = group(grp)
    r = results()[idx]
    gr = group_results(g, r)
    print(f'GROUP-{grp}')
    print(pretty_results(gr))
