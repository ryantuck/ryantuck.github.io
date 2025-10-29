songs_128 = open('songs-tournament-seeds.txt').read().splitlines()

matchups_64 = open('matchups-64.txt').read().splitlines()
matchups_32 = open('matchups-32.txt').read().splitlines()
matchups_16 = open('matchups-16.txt').read().splitlines()

songs_by_round = {}
songs_by_round['round-of-128'] = songs_128

x = 64
while x >= 1:
    matchups = open(f'matchups-{x}.txt').read().splitlines()
    songs = list(songs_by_round.values())[-1]
    songs_winners = []
    for idx, winner in enumerate(matchups):
        i = 0 if winner == 'a' else 1
        songs_winners.append(songs[2*idx+i])
    songs_by_round[f'round-of-{x}'] = songs_winners
    if x == 1:
        break
    x = int(x/2)


import json
print(json.dumps(songs_by_round))
