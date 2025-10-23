import sys, json

def track(data):
    track = data['track']
    return dict(
        id=track['id'],
        url=track['external_urls']['spotify'],
        title=track['name'],
        artists=[a['name'] for a in track['artists']],
    )


def track_str(t):
    artists = ', '.join(a for a in t['artists'])
    title = _tidy_title(t['title'])
    return f'{title} - {artists}'


def _tidy_title(song):
    just_song = song.split(" - ")[0] # [1:][0]
    just_song = just_song.split('feat')[0]
    just_song = just_song.split('(')[0]
    just_song = just_song.split('(feat')[0]
    just_song = just_song.strip()
    return just_song

t_fn_name = sys.argv[1]
t_fn = eval(t_fn_name)

for line in sys.stdin:
    data = json.loads(line)
    print(json.dumps(t_fn(data)))
