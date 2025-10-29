import sys, json

def read_jsonl(filepath):
    return [json.loads(line) for line in open(filepath).readlines()]


def song(song_title_str, songs_list):
    # print(song_title_str)
    title = ' - '.join(song_title_str.split(' - ')[1:])
    # print(title)
    if song_title_str == 'Immortal Technique - Dance with the Devil':
        # not gucci mane
        return next(s for s in songs_list if s['name'] == 'Dance with the Devil' and s['artists'][0]['name'] == 'Immortal Technique')
    return next(s for s in songs_list if s['name'] == title)



def read_stdin_list():
    return [line.strip() for line in sys.stdin]


songs_list = [x['track'] for x in read_jsonl('../rap.jsonl')]

def cli():
    old_fmt_titles = read_stdin_list()
    for ot in old_fmt_titles:
        print(json.dumps(song(ot, songs_list)))


if __name__ == '__main__':
    cli()
