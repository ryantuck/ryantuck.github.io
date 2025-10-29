results-round-2.json : groups-round-2.json rankings.txt play_group.py
	cat $< | python play_group.py | jq > $@

groups-round-2.json : results-round-1.json seed.py
	cat $< | python seed.py | jq > $@
