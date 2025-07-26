results-round-1.json : rankings.txt group-127 seed.py
	python seed.py | jq > $@

pretty-results.txt : results-round-1.json pretty.py
	cat $< | python pretty.py > $@

.PHONY : groups
groups : songs-round-1.txt
	split -d -l 4 -a 3 $< group-

groups-pretty.txt : group-127
	tail -n +1 group-* > $@

# songs-round-1.txt :
# 	shuf ../songs-sorted-512.txt > $@
