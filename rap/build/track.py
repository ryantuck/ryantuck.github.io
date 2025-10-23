import sys, json

def track(data):
    data = json.loads(data)
    track = data['track']
    return {
        'id': track['id'],
        'url': track['external_urls']['spotify'],
        'title': track['name'],
        'artists': [a['name'] for a in track['artists']],
    }

for line in sys.stdin:
    print(json.dumps(track(line)))
