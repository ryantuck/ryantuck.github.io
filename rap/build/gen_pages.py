import json

def squad_results():
    return json.load(open('squad-results.json'))

# ------------------------------------------------

def h1(s):
    return f'# {s}'

def h2(s):
    return f'## {s}'

def h3(s):
    return f'### {s}'

def h4(s):
    return f'#### {s}'

def b(s):
    return f'**{s}**'

def i(s):
    return f'_{s}_'

def strikethrough(s):
    return f'~~{s}~~'

def ol(strs):
    output = []
    for idx, s in enumerate(strs):
        line = f'{idx+1}. {s}'
        output.append(line)
    return '\n'.join(output)

def hr():
    return '---'

# ------------------------------------------------

def group_results_stylized(results):
    return [
        results[0],
        results[1],
        strikethrough(i(results[2])),
        strikethrough(i(results[3])),
    ]


def group_round_md_2(squad_name, group_round_results):
    output = []
    data = {
        '2 / X': list(group_round_results.values())[0],
        '2 / Y': list(group_round_results.values())[1],
    }
    for group_name, results in data.items():
        results = group_results_stylized(results)
        title = f'{squad_name.split("-")[1]} / {group_name.title()}'
        parts = [
            h2(title),
            ol(results),
        ]
        output += parts
    return '\n\n'.join(output)


def group_round_md_1(squad_name, group_round_results):
    output = []
    data = {
        '1 / A': list(group_round_results.values())[0],
        '1 / B': list(group_round_results.values())[1],
        '1 / C': list(group_round_results.values())[2],
        '1 / D': list(group_round_results.values())[3],
    }
    for group_name, results in data.items():
        results = group_results_stylized(results)
        title = f'{squad_name.split("-")[1]} / {group_name.title()}'
        parts = [
            h4(title),
            ol(results),
        ]
        output += parts
    return '\n\n'.join(output)


def squad_rankings_md(rankings):
    return '\n\n'.join([
        h1(f'1 - {rankings[0]}'),
        h2(f'2 - {rankings[1]}'),
        h3(f'3 - {rankings[2]}'),
        h4(f'4 - {rankings[3]}'),
    ])


def squad_page(squad_name, results):

    rankings = list(results['rankings'].values())[0]
    rankings_md = ol(b(s) for s in rankings)

    round_1 = results['round_1']
    round_2 = results['round_2']

    parts = [
        h1(squad_name.upper().replace('-',' ')),

        squad_rankings_md(rankings),

        # hr(),

        h3('_ ^ _ _ _ ^ _ _ _ ^ _ _ _ ^ _ _ '),

        # h2('Squad - Group Round of 8'),
        # h2(f'{squad_name.title()} - Group Round of 8'),
        group_round_md_2(squad_name, round_2),

        h3('_ ^ ^ _ _ ^ ^ _ _ ^ ^ _ _ ^ ^ _'),

        # hr(),

        # h3('Squad - Group Round of 16'),
        group_round_md_1(squad_name, round_1),

        hr(),
        '\n',
    ]

    return '\n\n'.join(parts)

# ------------------------------------------------

def cli():
    import sys
    squad_name = sys.argv[1]
    results = squad_results()[squad_name]
    page = squad_page(squad_name, results)
    print(page)


if __name__ == '__main__':
    cli()
