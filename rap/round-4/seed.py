"""
a.1.1
a.2.4
b.1.3
b.2.2
b.4.2
b.3.3
a.4.4
a.3.1

L1 - 1,2 5,6
L2 - 3,4 7,8

R1 - 2,1 6,5
R2 - 4,3 8,7

a.4.1
a.3.4
b.4.3
b.3.2
b.1.2
b.2.3
a.1.4
a.2.1

L3 - 1,2 5,6
L4 - 3,4 7,8

R3 - 2,1 6,5
R4 - 4,3 8,7
"""

import sys, json
tournament_seed_batches = json.loads(''.join(list(sys.stdin)))


def song(rank_grp_id, rank):
    return tournament_seed_batches[rank_grp_id][rank-1]


def rank_group_id(x,y):
    return f'rankings-{x}-{y}'


# 1 1,2 1v4
# 2 1,2 3v2
# 2 4,3 2v3
# 1 4,3 4v1

def ocho(x,y,t=False):

    a,b = 1,2
    c,d = 4,3
    if t:
        a,b = 4,3
        c,d = 1,2

    return [
        (rank_group_id(x,a), 1),
        (rank_group_id(x,b), 4),
        (rank_group_id(y,a), 3),
        (rank_group_id(y,b), 2),
        (rank_group_id(y,c), 2),
        (rank_group_id(y,d), 3),
        (rank_group_id(x,c), 4),
        (rank_group_id(x,d), 1),
    ]


octets = [
    ocho(1,2),
    ocho(5,6),
    ocho(3,4),
    ocho(7,8),
    ocho(1,2, True),
    ocho(5,6, True),
    ocho(3,4, True),
    ocho(7,8, True),
    ocho(2,1),
    ocho(6,5),
    ocho(4,3),
    ocho(8,7),
    ocho(2,1, True),
    ocho(6,5, True),
    ocho(4,3, True),
    ocho(8,7, True),
]

for octet in octets:
    for seed in octet:
        print(song(seed[0], seed[1]))
