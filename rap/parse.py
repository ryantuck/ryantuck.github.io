import sys


ABCD = ['a', 'b', 'c', 'd']


def parse_standings(results):

    standings = {x: [0,0,0] for x in ABCD}

    for result in results:
        assert len(result) == 3
        x,r,y = result
        if r == '-': # tie
            standings[x][2] += 1
            standings[y][2] += 1
            continue
        standings[x][0] += 1
        standings[y][1] += 1

    return standings


def points(wlt):
    return 3*wlt[0] + 1*wlt[2]


def songs(group_id):
    lines = [x.strip() for x in open(f'round-0-knockout/{group_id}').readlines()]
    assert len(lines) == 4
    return {x: song for x, song in zip(ABCD, lines)}


def parse(line):

    parts = line.split()
    assert len(parts) == 7
    group_id = parts[0]
    results = parts[1:]

    standings = parse_standings(results)
    song_titles = songs(group_id)

    pts = {x: points(wlt) for x, wlt in standings.items()}
    rankings = sorted(pts.items(), key=lambda x: x[1], reverse=True)

    print(group_id.upper())
    for idx, (x, n) in enumerate(rankings):
        print(idx+1, x, n, '-'.join(str(y) for y in standings[x]), song_titles[x])


def cli():
    lines = list(sys.stdin)
    for line in lines:
        parse(line)


if __name__ == '__main__':
    cli()
