import sys, json, argparse

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


def echo(d):
    return d


def ol(strs):
    output = []
    for idx, s in enumerate(strs):
        line = f'{idx+1}. {s}'
        output.append(line)
    return '\n'.join(output)


def i(s):
    return f'_{s}_'

def strikethrough(s):
    return f'~~{s}~~'



def group_results_stylized(results):
    return ol([
        results[0],
        results[1],
        strikethrough(i(results[2])),
        strikethrough(i(results[3])),
    ])


def json_graceful(lines):
    body = []
    results = []
    for line in lines:
        body.append(line)
        try:
            x = json.loads('\n'.join(body))
            results.append(x)
            body = []
        except:
            pass
    if body != []:
        raise Exception('\n'.join(body))
    return results

def track_id_map(tracks_list):
    return {track['title']: track['id'] for track in tracks_list}


parser = argparse.ArgumentParser()
parser.add_argument('transform_name')
parser.add_argument('-s', '--slurp', required=False, action='store_true')
args = parser.parse_args()

assert " " not in args.transform_name
transform_fn = eval(args.transform_name)

data = json_graceful(sys.stdin)
records = [transform_fn(record) for record in data]
if args.slurp:
    print(json.dumps(records))
else:
    for record in records:
        print(json.dumps(record))
