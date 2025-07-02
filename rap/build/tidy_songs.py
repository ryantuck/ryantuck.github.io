import json


def _tidy_song(song):
    just_song = song.split(" - ")[1:][0]
    just_song = just_song.split('feat')[0]
    just_song = just_song.split('(')[0]
    just_song = just_song.strip()
    return just_song


def get_results():
    data = json.load(open('../round-5-tournament/songs-by-round.json'))
    return [
        [_tidy_song(s) for s in songs]
        for songs in data.values()
    ]


print(json.dumps(get_results()))
