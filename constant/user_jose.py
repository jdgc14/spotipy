from models.user_free import UserFree

from constant.dua_lipa import lipa
from constant.minaj import minaj
from constant.bieber import bieber



jose_user = UserFree('jose', '12345', 'email@email.com')

jose_user.follow(lipa)

jose_user.follow(minaj)

jose_user.like_song(lipa.albums['dualipa_deluxe'].songs_playlist[5])

jose_user.like_song(lipa.albums['dualipa_deluxe'].songs_playlist[1])

jose_user.like_song(lipa.albums['dualipa_deluxe'].songs_playlist[11])

jose_user.like_song(bieber.albums['changes'].songs_playlist[11])

jose_user.like_song(bieber.albums['changes'].songs_playlist[3])

jose_user.like_song(minaj.albums['queen'].songs_playlist[3])

jose_user.like_song(minaj.albums['queen'].songs_playlist[15])

jose_user.create_playlist('music_new')

jose_user.playlists['music_new'].add_song(bieber.albums['changes'].songs_playlist[6])

jose_user.playlists['music_new'].add_song(bieber.albums['changes'].songs_playlist[2])

jose_user.playlists['music_new'].add_song(bieber.albums['changes'].songs_playlist[5])

jose_user.playlists['music_new'].add_song(bieber.albums['changes'].songs_playlist[0])

jose_user.playlists['music_new'].add_song(bieber.albums['changes'].songs_playlist[8])

jose_user.playlists['music_new'].add_song(bieber.albums['changes'].songs_playlist[10])

jose_user.playlists['music_new'].add_song(bieber.albums['changes'].songs_playlist[1])

jose_user.playlists['music_new'].add_song(lipa.albums['dualipa_deluxe'].songs_playlist[2])

jose_user.playlists['music_new'].add_song(lipa.albums['dualipa_deluxe'].songs_playlist[9])

jose_user.playlists['music_new'].add_song(lipa.albums['dualipa_deluxe'].songs_playlist[5])

jose_user.playlists['music_new'].add_song(lipa.albums['dualipa_deluxe'].songs_playlist[3])

jose_user.playlists['music_new'].add_song(minaj.albums['queen'].songs_playlist[2])

jose_user.playlists['music_new'].add_song(minaj.albums['queen'].songs_playlist[8])

jose_user.playlists['music_new'].add_song(minaj.albums['queen'].songs_playlist[1])

jose_user.playlists['music_new'].add_song(minaj.albums['queen'].songs_playlist[12])

jose_user.playlists['music_new'].show_songs()
jose_user.playlists['liked_songs'].show_songs()