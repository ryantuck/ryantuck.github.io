.PHONY : view
view :
	bat group-*

.PHONY : groups
groups : knockout-round.txt
	split -d -l 4 -a 2 knockout-round.txt group-

group-02-a-matchups.txt: # build on this
	cat results.txt | grep group-02 | sed -e 's/ /\n/g' | grep a
