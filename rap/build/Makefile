outputs : bracket.html squad-results.json all-squads.html x.html ko.html squad-round.html all.html

artist-counts.txt :
	jq . tracks.jsonl | jq '.artists | .[]' -r | sort | uniq -c | sort -nr > $@

all-squads.md :
	cat Squad-*.md > $@

all.md : header.md ko.md header-squad-round.md squad-round.md header-bracket-round.md x.md
	cat header.md ko.md header-squad-round.md squad-round.md header-bracket-round.md x.md > $@

squad-round.md : squad-results.json gen_pages.py
	cat $< \
		| jq 'keys | .[]' -r | sort -t- -k 2n \
		| xargs -I % python gen_pages.py % > $@

knockout-groups.md : knockout-results.json
	jq . knockout-results.json | python transform.py group_results_stylized | jq -r | sed -e 's/1\./\n1\./g' > $@

knockout-results.json :
	cat ../knockout-results-round-0.txt | grep -v GROUP | cut -c 13- | jq -R | jq -s | jq '_nwise(4)' > $@

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

