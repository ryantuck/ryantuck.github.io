import sys
import json


def print_pretty_group_results(grp_ranked):
    for rank, song in enumerate(grp_ranked):
        print(f'{rank+1}. {song}')


def print_pretty_all_results(results_full):
    for grp_id, songs in results_full.items():
        print(grp_id.upper())
        print_pretty_group_results(songs)
        print()

results_full = json.loads(''.join(line for line in sys.stdin))
print_pretty_all_results(results_full)
