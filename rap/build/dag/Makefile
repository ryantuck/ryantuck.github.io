dag.svg : dag.gv
	dot -Tsvg -o $@ $<

dag.gv : edges.gv
	echo "digraph {" > $@
	echo "rankdir=LR;" >> $@
	echo "bgcolor=transparent;" >> $@
	echo "node [fontname=\"Courier New\", shape=rectangle];" >> $@
	cat $< >> $@
	echo "}" >> $@

edges.gv : ../Makefile
	cat $< | grep "^[a-z]" |  python parse.py | jq '.[]' | jq -s | jq '.[] | "\"\(.source)\" -> \"\(.target)\";"' -r > $@


