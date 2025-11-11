outputs : all.html

all.html : all.md
	pandoc $< -f gfm --metadata title="Da Ultimate Rap Battle 2025" --css common.css -s -o $@

all.md : header.md header-knockout-round.md knockout-round.md header-squad-round.md squad-round.md header-bracket-round.md bracket-round.md player.html
	cat header.md header-knockout-round.md knockout-round.md header-squad-round.md squad-round.md header-bracket-round.md bracket-round.md player.html > $@

squad-round.md : squad-results.json gen_pages.py # squad-round.css
	echo '<link rel="stylesheet" href="squad-round.css">' > $@
	cat $< \
		| jq 'keys | .[]' -r | sort -t- -k 2n \
		| xargs -I % python gen_pages.py % >> $@

knockout-round.md : knockout-groups.md # knockout-round.css
	echo '<link rel="stylesheet" href="knockout-round.css">' > $@
	echo '<div id="knockout-round">' >> $@
	cat $< >> $@
	echo '</div>' >> $@

knockout-groups.md : knockout-results.json transform.py
	jq . knockout-results.json | python transform.py group_div | jq -r  > $@

bracket-round.md : bracket-results.md # bracket.css rounds-input.js
	echo '<link rel="stylesheet" href="bracket.css">' > $@
	echo '<script src="rounds-input.js"></script>' >> $@
	echo '<div id="bracket">' >> $@
	cat $< >> $@
	echo '</div>' >> $@


bracket-results.md : bracket-results.json
	cat $< | jq '.[]' -c \
		| python transform.py bracket_round_n_div \
		| jq '.[]' -r > $@

bracket-results.json : bracket-track-seeds.txt
	python play.py | jq > $@

bracket-track-seeds.txt : ../round-5-tournament/songs-tournament-seeds.txt
	cat $< | python db.py | python transform.py minitrack | python transform.py track_str | jq -r > $@

knockout-results.json : ../knockout-results-round-0.txt
	cat $< \
		| grep -v GROUP | cut -c 13- \
		| python db.py \
		| python transform.py minitrack | python transform.py track_str \
		| jq -s | jq '_nwise(4)' > $@


squad-results.json : gen_squads.py ../round-1/results-round-1.json ../round-2/results-round-2.json ../round-3/tournament-seed-batches.yml
	python gen_squads.py | jq > $@



track-str-id-map.json : tracks.jsonl
	cat $< | jq -c | python transform.py -s track_str_id_map | jq > $@

track-str-map.json : tracks.jsonl
	jq . $< -c |  python transform.py track_str_map | jq -r | sort > $@

tracks.txt : tracks.jsonl
	jq . $< -c |  python transform.py track_str | jq -r | sort > $@

tracks.jsonl : ../rap.jsonl
	jq . $< -c | python transform.py track | jq -c > $@

tracks-in-order.jsonl : ../rap.jsonl
	cat ../knockout-results-round-0.txt | cut -c 13- | grep . | p db.py  | p transform.py minitrack | p transform.py track_str | jq -r
