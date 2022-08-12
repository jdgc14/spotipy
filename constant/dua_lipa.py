import random

from models.playlist import PlayList
from models.artist import Artist
from models.song import Song
from constant import bios

lipa = Artist('dualipa', 'dua1234', 'dualipa@email.com', bios.dua_bio)

dualipa_deluxe = [
	['Genesis', '3:25'],
	['Lost in Your Light', '3:23'],
	['Hotter than Hell', '3:07'],
	['Be the One', '3:22'],
	['IDGAF', '3:38'],
	['Blow Your Mind', '2:58'],
	['Garden', '3:47'],
	['No Goodbyes', '3:36'],
	["Thinking 'Bout You", '2:51'],
	['New Rules', '3:32'],
	['Begging', '3:14'],
	['Homesick', '3:50'],
]

future_nostalgia = [
	['Future Nostalgia', '3:04'],
	["Don't Start Now Lipa", '3:03'],
	["Cool", '3:29'],
	["Physical", '3:13'],
	["Levitating", '3:23'],
	['Pretty Please', '3:14'],
	["Hallucinate", '3:28'],
	['Love Again', '4:18'],
	['Break My Heart', '3:41'],
	['Good in Bed', '3:38'],
	['Boys Will Be Boys', '2:46']
]

lipa.add_album_songs('dualipa_deluxe', dualipa_deluxe)

lipa.add_album_songs('future_nostalgia', future_nostalgia)

#Single, album is None
Song.create('Scared to Be Lonely', '3:40', lipa, 'letra de scared to be lonely')


this_is_dualipa=PlayList.create('this_is_dualipa')


# dont work for one album
for album in lipa.albums:
	for song in random.choices(lipa.albums[album].songs_playlist, k=4):
		this_is_dualipa.add_song(song)