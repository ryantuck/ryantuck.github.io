all : books 2024

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
	the-stranger.html\
	the-brothers-karamazov.html \
	the-handmaids-tale.html \
	identity.html \
	snow-crash.html \
	grapes-of-wrath.html


war-and-peace.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find books/war-and-peace/* | sort -V | xargs -I % echo '<img src="%" />' >> $@

moby-dick.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find books/moby-dick/* | sort -V | xargs -I % echo '<img src="%" />' >> $@

candide.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find books/candide/* | sort -V | xargs -I % echo '<img src="%" />' >> $@

catcher-in-the-rye.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find books/catcher-in-the-rye/* | sort -V | xargs -I % echo '<img src="%" />' >> $@

watership-down.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find books/watership-down/* | sort -V | xargs -I % echo '<img src="%" />' >> $@

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

the-brothers-karamazov.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find books/bro-k/* | sort -V | xargs -I % echo '<img src="%" />' >> $@

the-handmaids-tale.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find books/handmaids-tale/* | sort -V | xargs -I % echo '<img src="%" />' >> $@

identity.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find books/identity/* | sort -V | xargs -I % echo '<img src="%" />' >> $@

snow-crash.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find books/snow-crash/* | sort -V | xargs -I % echo '<img src="%" />' >> $@

grapes-of-wrath.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find books/grapes-of-wrath/* | sort -V | xargs -I % echo '<img src="%" />' >> $@





# ----------------

2024 : \
	2024-01.html \
	2024-02.html \
	2024-03.html \
	2024-04.html \
	2024-05.html \
	2024-06.html \
	2024-07.html \
	2024-08.html \
	2024-09.html \
	2024-10.html \
	2024-11.html \
	2024-12.html \
	2024-jackson-hole.html


2024-01.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find 2024-01/ -type f | sort -V | xargs -I % echo '<img src="%" />' >> $@

2024-02.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find 2024-02/ -type f | sort -V | xargs -I % echo '<img src="%" />' >> $@

2024-03.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find 2024-03/ -type f | sort -V | xargs -I % echo '<img src="%" />' >> $@

2024-04.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find 2024-04/ -type f | sort -V | xargs -I % echo '<img src="%" />' >> $@

2024-05.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find 2024-05/ -type f | sort -V | xargs -I % echo '<img src="%" />' >> $@

2024-06.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find 2024-06/ -type f | sort -V | xargs -I % echo '<img src="%" />' >> $@

2024-07.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find 2024-07/ -type f | sort -V | xargs -I % echo '<img src="%" />' >> $@

2024-08.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find 2024-08/ -type f | sort -V | xargs -I % echo '<img src="%" />' >> $@

2024-09.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find 2024-09/ -type f | sort -V | xargs -I % echo '<img src="%" />' >> $@

2024-10.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find 2024-10/ -type f | sort -V | xargs -I % echo '<img src="%" />' >> $@

2024-11.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find 2024-11/ -type f | sort -V | xargs -I % echo '<img src="%" />' >> $@

2024-12.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find 2024-12/ -type f | sort -V | xargs -I % echo '<img src="%" />' >> $@

2024-jackson-hole.html :
	rm -f $@
	echo "<link href="book-page.css?no=cache" rel="stylesheet" type="text/css" />" >> $@
	find 2024-jackson-hole/ -type f | sort -V | xargs -I % echo '<img src="%" />' >> $@




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

# ---------------

lit.html : lit.md
	pandoc $< -s -o $@

# ---------------

notes/%.html : notes/md/%.md
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
	pip install google-api-python-client

serve :
	python -m http.server
