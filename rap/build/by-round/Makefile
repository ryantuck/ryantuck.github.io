# ----------------------------------------------------
# Artists by round breakdown - WIP
# ----------------------------------------------------

artist-counts.txt : artists-by-round-all.txt
	cat $< | sort | uniq -c | sort -nr > $@

artists-by-round-all.txt : ../tracks.jsonl
	jq . $< | jq '.artists | .[]' -r | sort  > $@

artists-by-round-x : \
	artists-by-round-all.txt \
	artists-by-round-knockout.txt \
	artists-by-round-round-1.txt \
	artists-by-round-round-2.txt \
	artists-by-round-bracket-128.txt \
	artists-by-round-bracket-64.txt \
	artists-by-round-bracket-32.txt \
	artists-by-round-bracket-16.txt \
	artists-by-round-bracket-8.txt \
	artists-by-round-bracket-4.txt \
	artists-by-round-bracket-2.txt \
	artists-by-round-bracket-1.txt

artists-by-round-%.txt : tracks-by-round-%.txt
	cat $< | sed -e 's/^.* - //' | sort \
		| jq -R | jq 'split(", ")' | jq '.[]' -r \
		| sort > $@

tracks-by-round-txt : \
	tracks-by-round-knockout.txt \
	tracks-by-round-round-1.txt \
	tracks-by-round-round-2.txt \
	tracks-by-round-bracket-x

tracks-by-round-knockout.txt : ../knockout-results.json
	jq . $< | jq '.[2:] | .[]' -r | sort > $@

tracks-by-round-round-1.txt : ../squad-results.json
	jq . $< \
		| jq '.[].round_1 | .[] | .[2:] | .[]' -r \
		| sort | less -r > $@

tracks-by-round-round-2.txt : ../squad-results.json
	jq . $< \
		| jq '.[].round_2 | .[] | .[2:] | .[]' -r \
		| sort | less -r > $@

tracks-by-round-bracket-x : \
	tracks-by-round-bracket-128.txt \
	tracks-by-round-bracket-64.txt \
	tracks-by-round-bracket-32.txt \
	tracks-by-round-bracket-16.txt \
	tracks-by-round-bracket-8.txt \
	tracks-by-round-bracket-4.txt \
	tracks-by-round-bracket-2.txt \
	tracks-by-round-bracket-1.txt

tracks-by-round-bracket-128.txt : bracket-round-of-128.txt bracket-round-of-64.txt
	diff bracket-round-of-128.txt bracket-round-of-64.txt | grep "^<" | cut -c 3- > $@

tracks-by-round-bracket-64.txt : bracket-round-of-64.txt bracket-round-of-32.txt
	diff bracket-round-of-64.txt bracket-round-of-32.txt | grep "^<" | cut -c 3- > $@

tracks-by-round-bracket-32.txt : bracket-round-of-32.txt bracket-round-of-16.txt
	diff bracket-round-of-32.txt bracket-round-of-16.txt | grep "^<" | cut -c 3- > $@

tracks-by-round-bracket-16.txt : bracket-round-of-16.txt bracket-round-of-8.txt
	diff bracket-round-of-16.txt bracket-round-of-8.txt | grep "^<" | cut -c 3- > $@

tracks-by-round-bracket-8.txt : bracket-round-of-8.txt bracket-round-of-4.txt
	diff bracket-round-of-8.txt bracket-round-of-4.txt | grep "^<" | cut -c 3- > $@

tracks-by-round-bracket-4.txt : bracket-round-of-4.txt bracket-round-of-2.txt
	diff bracket-round-of-4.txt bracket-round-of-2.txt | grep "^<" | cut -c 3- > $@

tracks-by-round-bracket-2.txt : bracket-round-of-2.txt bracket-round-of-1.txt
	diff bracket-round-of-2.txt bracket-round-of-1.txt | grep "^<" | cut -c 3- > $@

tracks-by-round-bracket-1.txt : bracket-round-of-1.txt
	cp $< $@

bracket-round-of-x : \
	bracket-round-of-128.txt \
	bracket-round-of-64.txt \
	bracket-round-of-32.txt \
	bracket-round-of-16.txt \
	bracket-round-of-8.txt \
	bracket-round-of-4.txt \
	bracket-round-of-2.txt \
	bracket-round-of-1.txt

bracket-round-of-128.txt : ../bracket-results.json
	jq . $< | jq '."round-of-128" | .[]' -r | sort > $@

bracket-round-of-64.txt : ../bracket-results.json
	jq . $< | jq '."round-of-64" | .[]' -r | sort > $@

bracket-round-of-32.txt : ../bracket-results.json
	jq . $< | jq '."round-of-32" | .[]' -r | sort > $@

bracket-round-of-16.txt : ../bracket-results.json
	jq . $< | jq '."round-of-16" | .[]' -r | sort > $@

bracket-round-of-8.txt : ../bracket-results.json
	jq . $< | jq '."round-of-8" | .[]' -r | sort > $@

bracket-round-of-4.txt : ../bracket-results.json
	jq . $< | jq '."round-of-4" | .[]' -r | sort > $@

bracket-round-of-2.txt : ../bracket-results.json
	jq . $< | jq '."round-of-2" | .[]' -r | sort > $@

bracket-round-of-1.txt : ../bracket-results.json
	jq . $< | jq '."round-of-1" | .[]' -r | sort > $@


lil-wayne-by-round.txt :
	grep -o "Lil Wayne" \
		artists-by-round-all.txt \
		artists-by-round-knockout.txt \
		artists-by-round-round-1.txt \
		artists-by-round-round-2.txt \
		artists-by-round-bracket-128.txt \
		artists-by-round-bracket-64.txt \
		artists-by-round-bracket-32.txt \
		artists-by-round-bracket-16.txt \
		artists-by-round-bracket-8.txt \
		artists-by-round-bracket-4.txt \
		artists-by-round-bracket-2.txt \
		artists-by-round-bracket-1.txt \
		| uniq -c

