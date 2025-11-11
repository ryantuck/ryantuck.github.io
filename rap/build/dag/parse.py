def parse_make_line(make_line: str):

    make_line = make_line.split('#')[0]

    parts = [x.strip() for x in make_line.split(':')]
    left = parts[0]
    if len(parts) == 1:
        return []
    right = [x.strip() for x in parts[1].split(' ')]

    target = left
    prereqs = right
    return [{'source': prereq, 'target': target} for prereq in prereqs]


import sys,json
for line in sys.stdin:
    print(json.dumps(parse_make_line(line.strip())))
