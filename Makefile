books : \
	war-and-peace.html \
	moby-dick.html \
	candide.html \
	catcher-in-the-rye.html \
	watership-down.html \
	fight-club.html \
	atlas-shrugged.html \
	1984.html \
	a-tale-of-two-cities.html \
	fahrenheit-451.html \
	brave-new-world.html \
	lord-of-the-flies.html \
	we.html \
	frankenstein.html \
	the-dispossessed.html \
	the-republic.html \
	two-cheers-for-anarchism.html \
	dune.html \
	dune-messiah.html \
	children-of-dune.html \
	god-emperor-of-dune.html \
	heretics-of-dune.html \
	chapterhouse-dune.html \
	old-man-and-the-sea.html \
	the-stranger.html

war-and-peace.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find books/war-and-peace/* | sort | xargs -I % echo '<img src="%" />' >> $@

moby-dick.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find books/moby-dick/* | sort | xargs -I % echo '<img src="%" />' >> $@

candide.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find books/candide/* | sort | xargs -I % echo '<img src="%" />' >> $@

catcher-in-the-rye.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find books/catcher-in-the-rye/* | sort | xargs -I % echo '<img src="%" />' >> $@

watership-down.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find books/watership-down/* | sort | xargs -I % echo '<img src="%" />' >> $@

fight-club.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."Fight Club" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

atlas-shrugged.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."Atlas Shrugged" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

1984.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."1984" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

brave-new-world.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."Brave New World" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

a-tale-of-two-cities.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."A Tale of Two Cities" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

fahrenheit-451.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."Fahrenheit 451" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

lord-of-the-flies.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."Lord of the Flies" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

we.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."We" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

the-republic.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."The Republic" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

the-dispossessed.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."The Dispossessed" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

frankenstein.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."Frankenstein" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

two-cheers-for-anarchism.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."two-cheers-for-anarchism-highlights" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

dune.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."Dune" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

dune-messiah.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."Dune Messiah" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

children-of-dune.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."Children of Dune" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

god-emperor-of-dune.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."God Emperor of Dune" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

heretics-of-dune.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."Heretics of Dune" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

chapterhouse-dune.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."Chapterhouse: Dune" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

old-man-and-the-sea.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."Old Man and the Sea" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@

the-stranger.html : drive-structure.json
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	cat $< | jq '."The Stranger" | .[]' -r | xargs -I % echo '<img src="%" />' >> $@







# ----------------

2024-10.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find 2024-10/ -type f | sort | xargs -I % echo '<img src="%" />' >> $@






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

country.html : country.md
	pandoc $< -s -o $@

# ----------------

nashville.html : nashville.md
	pandoc $< -s -o $@

# ----------------
etc.json : etc.yml
	yq r -j $< > $@

# TODO - most elegant way to account for / interact with subdir makefiles?
spotify-playlists.html : 
	$(MAKE) -C spotify playlists.html
	cp spotify/playlists.html $@
# ----------------

drive-structure.json : drive.py
	python drive.py | jq > $@

.PHONY : install serve

install : 
	npm install -g http-server
	pip install google-api-python-client

serve :
	http-server -c-1
