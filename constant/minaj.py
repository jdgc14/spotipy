import random

from models.playlist import PlayList
from models.artist import Artist
from models.song import Song
from constant import bios

minaj = Artist('nickyminaj', 'minaj098', 'nickyminaj@email.com', bios.minaj_bio)

queen_list = (
	['Ganja Burn', '4:54'],
	['Majesty', '4:55'],
	['Barbie Dreams', '3:18'],
	['Rich Sex', '3:12'],
	['Hard White', '3:13'],
	['Bed', '3:09'],
	['Thought I Knew You', '4:39'],
	['Run & Hide', '2:34'],
	['Chun Swae', '6:10'],
	['Chun-Li', '3:11'],
	['LLC', '3:41'],
	['Good Form', '3:19'],
	['Nip Tuck', '3:27'],
	['2 Lit 2 Late Interlude', '0:55'],
	['Come See About Me', '4:06'],
	['Sir', '3:44'],
	['Miami', '3:10'],
	['Coco Chanel', '3:44'],
	['Inspirations Outro', '0:58'],
)


# minaj.add_album('queen')
minaj.add_album_songs('queen', queen_list)

this_is_minaj=PlayList.create('this_is_minaj')


for song in random.choices(minaj.albums['queen'].songs_playlist, k=4):
	this_is_minaj.add_song(song)