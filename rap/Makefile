songs.txt : songs.jsonl
	cat $< | jq -r '"\(.artist) - \(.title)"' > $@

# NOTE shuf
songs.jsonl : rap.jsonl
	cat $< | jq -c '{id: .track.id, title: .track.name, artist: .track.artists[0].name}' | shuf > $@
