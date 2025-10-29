import sys, json

results_round_2 = json.loads(''.join(list(sys.stdin)))

n_groups = len(list(results_round_2.keys()))
n_batches = int(n_groups / 2)

def batch(i):
    start_idx = i*2
    end_idx = start_idx + 2
    grp_ids = list(results_round_2.keys())[start_idx:end_idx]
    return {
        grp_id: songs
        for grp_id, songs in results_round_2.items()
        if grp_id in grp_ids
    }


def qualifiers(b):
    x = list(b.values())
    return x[0][0:2] + x[1][0:2]


# rankings-1-4 ... rankings - 8-4
def tournament_inputs():
    output = {}
    for i in range(n_batches):
        b = batch(i)
        r = i % 4
        g = int((i-r)/4)
        output[f'rankings-{g+1}-{r+1}'] = qualifiers(b)
    return output


# b = batch(3)
# print(json.dumps(b))
# print(json.dumps(new_groups(b)))

print(json.dumps(tournament_inputs()))
