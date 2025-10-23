outputs : bracket.html squad-results.json all-squads.html

all-squads.md :
	cat Squad-*.md > $@

.PHONY : md-pages
md-pages : squad-results.json
	jq 'keys | .[]' -r $< | xargs -I % sh -c 'python gen_pages.py % > %.md'

%.html : %.md
	pandoc $< -f gfm --css bracket.css -s -o $@

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

