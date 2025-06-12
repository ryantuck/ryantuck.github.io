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

def ocho(x):

    y = x+1

    print(rank_group_id(x,1), 1)
    print(rank_group_id(x,2), 4)

    print(rank_group_id(y,1), 3)
    print(rank_group_id(y,2), 2)

    print(rank_group_id(y,4), 2)
    print(rank_group_id(y,3), 3)

    print(rank_group_id(x,4), 4)
    print(rank_group_id(x,3), 1)







print(song('rankings-8-3', 3))

ocho(1)
ocho(5)
ocho(3)
ocho(7)


