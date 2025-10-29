unranked-batches.yml : results-round-2.json
	cat $< | jq | python gen_tournament.py | jq | yq -P > $@
