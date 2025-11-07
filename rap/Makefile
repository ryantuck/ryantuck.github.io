outputs : index.html css js crosshairs.png

index.html : build/all.html
	cp $< $@

crosshairs.png : build/crosshairs.png
	cp $< $@

css : knockout-round.css squad-round.css bracket.css common.css

js : rounds-input.js player.js

%.css : build/%.css
	cp $< $@

%.js : build/%.js
	cp $< $@

# -------------------------------------------

knockout-round-0-eliminated.txt : knockout-results-round-0.txt
	cat $< | grep "^3\|^4" | cut -c 13- | sort > $@

knockout-results-round-0.txt : round-0-knockout/results.txt
	cat $< | grep group- | python parse.py > $@

songs.txt : songs.jsonl
	cat $< | jq -r '"\(.artist) - \(.title)"' > $@

# NOTE shuf
songs.jsonl : rap.jsonl
	cat $< | jq -c '{id: .track.id, title: .track.name, artist: .track.artists[0].name}' | shuf > $@

songs-sorted-512.txt :
	diff sorted-songs.txt knockout-round-0-eliminated.txt | grep "<" | cut -c 3- > $@

rap.jsonl :
	p spotify.py playlist-tracks 1keGFxmCHN7V7tmLf3vYuY > $@
