


def results():
    return open('results.txt').read().splitlines()


def group(x):
    return open(f'group-{x}').read().splitlines()


def group_results(g, r):
    return sorted(zip(r,g), key=lambda x: x[0])


def pretty_results(gr):
    for r, s in gr:
        print(f'{r}. {s}')


g = group('000')
r = results()[0]
gr = group_results(g, r)
print(pretty_results(gr))
