import json
import yaml

from pydantic import BaseModel

import db, transform


def _track(song):
    # TODO - rock superstar, dance w the devil, others?
    return transform.track_str(transform.minitrack(db.song(song, db.songs_list)))

# STATE =================================================================

def results_round_1():
    return json.load(open('../round-1/results-round-1.json'))


def results_round_2():
    return json.load(open('../round-2/results-round-2.json'))


def results_round_3_rankings():
    return yaml.safe_load(open('../round-3/tournament-seed-batches.yml'))


class Results(BaseModel):
    round_1: dict
    round_2: dict
    rankings: dict


all_results = Results(
    round_1=results_round_1(),
    round_2=results_round_2(),
    rankings=results_round_3_rankings(),
)

def squad_results(n):
    ref_idx = n
    round_1_tuples = dict(list(all_results.round_1.items())[4*n:4*n+4])
    round_2_tuples = dict(list(all_results.round_2.items())[2*n:2*n+2])
    rankings_group = dict(list(all_results.rankings.items())[n:n+1])
    return Results(
        round_1={k:[_track(s) for s in songs] for k,songs in round_1_tuples.items()},
        round_2={k:[_track(s) for s in songs] for k,songs in round_2_tuples.items()},
        rankings={k: [_track(s) for s in songs] for k,songs in rankings_group.items()},
    )


def all_squad_results():
    output = {}
    for i in range(32):
        results = squad_results(i)
        output[f'Squad-{i}'] = results.model_dump()
    return output

r = all_squad_results()
print(json.dumps(r))
