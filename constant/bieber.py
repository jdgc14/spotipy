import random

from models.playlist import PlayList
from models.artist import Artist
from models.song import Song
from constant import bios

bieber = Artist('justinbieber', 'bieber911', 'justinbieber@email.com', bios.bieber_bio)

changes_list = [
	["All Around Me", '2:16'],
	["Habitual", '2:48'],
	["Come Around Me", '3:20'],
	["Intentions", '3:32'],
	["Yummy", '3:28'],
	["Available", '3:15'],
	["Forever", '3:39'],
	["Running Over", '2:59'],
	["Take It Out on Me", '2:58'],
	["Second Emotion", '3:22'],
	["Get Me", '3:05'],
	["E.T.A.", '2:56'],
	["Changes", '2:15'],
	["Confirmation", '2:50'],
	["That's What Love Is", '2:45'],
	["At Least for Now", '2:29'],
]

bieber.add_album_songs('changes', changes_list)

this_is_bieber=PlayList.create('this_is_bieber')


for song in random.choices(bieber.albums['changes'].songs_playlist, k=4):
	this_is_bieber.add_song(song)