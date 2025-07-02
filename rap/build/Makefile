bracket.txt : bracket-data.json asciibracket.py
	cat $< | python asciibracket.py > $@

bracket-data.json : songs-by-round.json tidy_songs.py
	cat $< | python tidy_songs.py > $@
