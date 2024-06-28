moby-dick.html :
	rm -f $@
	find books/moby-dick/* | sort | xargs -I % echo '<img src="%" />' >> $@

# ----------------

.PHONY : install serve

install : 
	npm install -g http-server

serve :
	http-server -c-1
