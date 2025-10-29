songs-tournament-seeds.txt : tournament-seed-batches.json
	cat $< | python seed.py > $@

tournament-seed-batches.json : tournament-seed-batches.yml
	yq . $< -o json > $@
