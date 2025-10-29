import sys, json, argparse

def track(data):
    track = data['track']
    return dict(
        id=track['id'],
        url=track['external_urls']['spotify'],
        title=track['name'],
        artists=[a['name'] for a in track['artists']],
    )


def minitrack(track):
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

    # handle edge-cases with parentheses
    if '(Rock) Superstar' in song:
        return '(Rock) Superstar'
    if 'Colt 45' in song:
        return 'Crazy Rap (Colt 45 & 2 Zig Zags)'

    just_song = song.split(" - ")[0]
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



def entry_with_spans(entry):
    parts = entry.split(' - ')
    assert len(parts) == 2 # ?
    title = parts[0]
    artists = ' - ' + parts[1]
    return ''.join([
        f'<span class="title">{title}</span>',
        f'<span class="artists">{artists}</span>',
    ])

def bracket_track_div(track):
    return f'<div>{entry_with_spans(track)}</div>'


def bracket_round_n_div(tracks):
    return [f'<div class="b">'] + [bracket_track_div(t) for t in tracks] + ['</div>']




def group_results_stylized(results):
    results = [entry_with_spans(e) for e in results]
    return [
        results[0],
        results[1],
        strikethrough(i(results[2])),
        strikethrough(i(results[3])),
    ]


def group_div(results):
    return '\n\n'.join([
        '<div>',
        ol(group_results_stylized(results)),
        '</div>',
        '\n',
    ])


def ko_round_body(all_group_divs):
    return '\n\n'.join([
        '<div id="container" style="display:flex;flex-flow:row wrap;justify-content:center;gap:5vh">',
        group_div(results),
        '</div>',
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

def parse_make_line(make_line: str):

    parts = [x.strip() for x in make_line.split(':')]
    left = parts[0]
    if len(parts) == 1:
        return []
    right = [x.strip() for x in parts[1].split(' ')]

    target = left
    prereqs = right
    return [{'source': prereq, 'target': target} for prereq in prereqs]

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('transform_name')
    parser.add_argument('-s', '--slurp', required=False, action='store_true')
    parser.add_argument('-r', '--raw', required=False, action='store_true')
    args = parser.parse_args()

    assert " " not in args.transform_name
    transform_fn = eval(args.transform_name)

    data = json_graceful(sys.stdin)
    records = [transform_fn(record) for record in data]
    if args.raw:
        print(records)
    elif args.slurp: # logic?
        print(json.dumps(records))
    else:
        for record in records:
            print(json.dumps(record))


if __name__ == '__main__':
    cli()
