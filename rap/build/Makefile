outputs : bracket.txt knockout-groups.html squad-round.html bracket-round.html all.html

%.html : %.md
	pandoc $< -f gfm --css bracket.css -s -o $@


dag.svg : dag.gv
	dot -Tsvg -o $@ $<

dag.gv : edges.gv
	echo "digraph {" > $@
	echo "rankdir=LR;" >> $@
	echo "bgcolor=transparent;" >> $@
	echo "node [fontname=\"Courier New\", shape=rectangle];" >> $@
	cat $< >> $@
	echo "}" >> $@

edges.gv : Makefile
	cat Makefile | grep "^[a-z]" | jq -R | python transform.py parse_make_line | jq '.[]' | jq -s | jq '.[] | "\"\(.source)\" -> \"\(.target)\";"' -r > edges.gv

artist-counts.txt : tracks.jsonl
	jq . tracks.jsonl | jq '.artists | .[]' -r | sort | uniq -c | sort -nr > $@

all.md : header.md header-knockout-round.md knockout-round.md header-squad-round.md squad-round.md header-bracket-round.md bracket-round.md
	cat header.md header-knockout-round.md knockout-round.md header-squad-round.md squad-round.md header-bracket-round.md bracket-round.md > $@

squad-round.md : squad-results.json gen_pages.py
	cat $< \
		| jq 'keys | .[]' -r | sort -t- -k 2n \
		| xargs -I % python gen_pages.py % > $@

knockout-round.md : knockout-groups.md knockout-round.css
	echo '<link rel="stylesheet" href="knockout-round.css">' > $@
	echo '<div id="container" style="display:flex;flex-flow:row wrap;justify-content:center;gap:5vh">' >> $@
	cat $< >> $@
	echo '</div>' >> $@

knockout-groups.md : knockout-results.json transform.py
	jq . knockout-results.json | python transform.py group_div | jq -r  > $@

bracket-round.md : bracket-results.md
	echo '<link rel="stylesheet" href="bracket.css">' > $@
	echo '<div id="bracket-round" style="display:flex">' > $@
	cat $< >> $@
	echo '</div>' >> $@


bracket-results.md : bracket-results.json
	cat $< | jq '.[]' -c | python transform.py bracket_round_n_div | jq '.[]' -r > $@

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


squad-results.json : gen_squads.py
	python gen_squads.py | jq > $@

bracket.txt : bracket-data.json asciibracket.py
	cat $< | python asciibracket.py > $@

bracket-data.json : songs-by-round.json tidy_songs.py
	cat $< | python tidy_songs.py > $@

tracks.jsonl : ../rap.jsonl
	jq . $< -c | python transform.py track | jq -c > $@

tracks.txt : tracks.jsonl
	jq . $< -c |  python transform.py track_str | jq -r | sort > $@

tracks-in-order.jsonl : ../rap.jsonl
	cat ../knockout-results-round-0.txt | cut -c 13- | grep . | p db.py  | p transform.py minitrack | p transform.py track_str | jq -r

















# all-squads.md :
# 	cat Squad-*.md > $@



# .PHONY : md-pages
# md-pages : squad-results.json
# 	jq 'keys | .[]' -r $< | xargs -I % sh -c 'python gen_pages.py % > %.md'








# Helpful artifacts to generate possibly, but not final?

# knockout-round.html : ../knockout-results-round-0.txt
# 	pandoc $< --css bracket.css -s -o $@
# 	# bypassing md layer
# 	# echo '<h1>Knockout Round</h1>' 			> $@
# 	# echo '<pre style="white-space:pre">' 	>> $@
# 	# cat $< 									>> $@
# 	# echo '</pre>' 							>> $@

# bracket.html : bracket.txt
# 	# bypassing md layer
# 	echo '<pre style="white-space:pre">' 	> $@
# 	cat $< 									>> $@
# 	echo '</pre>' 							>> $@

