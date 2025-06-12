import glob
import json, sys

groups_round_2 = json.loads(''.join(list(sys.stdin)))


def group_ids():
    return list(groups_round_2.keys())


def rankings():
    lines = open('rankings.txt').read().splitlines()
    assert all(len(line) == 4 for line in lines)
    assert all(set(line) == set('1234') for line in lines)
    return lines


def group(grp_id):
    return groups_round_2[grp_id]


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
