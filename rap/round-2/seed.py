# every four groups, create two new groups - 1212, 2121 rank

import sys, json
results_round_1 = json.loads(''.join(line for line in sys.stdin))

n_groups = len(results_round_1) # 128
n_batches = int(n_groups / 4) # 32

def batch(i):
    start_idx = i*4
    end_idx = start_idx + 4
    grp_ids = list(results_round_1.keys())[start_idx:end_idx]
    return {
        grp_id: songs
        for grp_id, songs in results_round_1.items()
        if grp_id in grp_ids
    }


def new_batch_groups(b):
    x = list(b.values())
    return {
        'a': [x[0][0], x[1][1], x[2][0], x[3][1]],
        'b': [x[0][1], x[1][0], x[2][1], x[3][0]],
    }


def round_2_groups():
    output = {}
    for i in range(n_batches):
        b = batch(i)
        grps = new_batch_groups(b)
        output[f'group-2-{i*2+1}'] = grps['a']
        output[f'group-2-{i*2+2}'] = grps['b']
    return output


# b = batch(3)
# print(json.dumps(b))
# print(json.dumps(new_groups(b)))

print(json.dumps(round_2_groups()))
