books : war-and-peace.html moby-dick.html

war-and-peace.html :
	rm -f $@
	find books/war-and-peace/* | sort | xargs -I % echo '<img src="%" />' >> $@

moby-dick.html :
	rm -f $@
	find books/moby-dick/* | sort | xargs -I % echo '<img src="%" />' >> $@

# ----------------

# # TODO jinja
# country-music.html : country-stuff
# 	echo '<img src="" />' > $@

# TODO compress images upon aliasing
country-stuff : country-bracket-1.jpg country-bracket-2.jpg country-bracket-3.jpg country-bracket-4.jpg country-top-8.jpg

country-top-8.jpg : country-music/IMG_5492.jpeg
	cp $< $@

country-bracket-1.jpg : country-music/IMG_5488.jpeg
	cp $< $@

country-bracket-2.jpg : country-music/IMG_5489.jpeg
	cp $< $@

country-bracket-3.jpg : country-music/IMG_5490.jpeg
	cp $< $@

country-bracket-4.jpg : country-music/IMG_5491.jpeg
	cp $< $@


# ----------------

.PHONY : install serve

install : 
	npm install -g http-server

serve :
	http-server -c-1
