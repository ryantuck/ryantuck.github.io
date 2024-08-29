books : war-and-peace.html moby-dick.html candide.html catcher-in-the-rye.html watership-down.html

war-and-peace.html :
	rm -f $@
	find books/war-and-peace/* | sort | xargs -I % echo '<img src="%" />' >> $@

moby-dick.html :
	rm -f $@
	find books/moby-dick/* | sort | xargs -I % echo '<img src="%" />' >> $@

candide.html :
	rm -f $@
	find books/candide/* | sort | xargs -I % echo '<img src="%" />' >> $@

catcher-in-the-rye.html :
	rm -f $@
	find books/catcher-in-the-rye/* | sort | xargs -I % echo '<img style="max-width: 400px" src="%" />' >> $@

watership-down.html :
	rm -f $@
	find books/watership-down/* | sort | xargs -I % echo '<img src="%" />' >> $@


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
etc.json : etc.yml
	yq r -j $< > $@

# TODO - most elegant way to account for / interact with subdir makefiles?
spotify-playlists.html : 
	$(MAKE) -C spotify playlists.html
	cp spotify/playlists.html $@
# ----------------

.PHONY : install serve

install : 
	npm install -g http-server
	pip install google-api-python-client

serve :
	http-server -c-1
