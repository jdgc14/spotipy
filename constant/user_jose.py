from models.user_free import UserFree
from constant.dua_lipa import lipa
from constant.minaj import minaj
from constant.bieber import bieber

print('Welcome to Spotipy')

print('\n')

print('----------------------------------')
print('----------------------------------')

print('user_free section')

jose_user = UserFree('jose', '12345', 'email@email.com')

print(jose_user, 'user free created')

print()

print(jose_user.follow(lipa))

print(jose_user.follow(minaj))

print(jose_user.follow(bieber))

print(jose_user.follow(bieber))

print()

print(jose_user.like_song(lipa.albums['dualipa_deluxe'].songs_playlist[5]))

print(jose_user.like_song(lipa.albums['dualipa_deluxe'].songs_playlist[1]))

print(jose_user.like_song(lipa.albums['dualipa_deluxe'].songs_playlist[11]))

print(jose_user.like_song(lipa.albums['dualipa_deluxe'].songs_playlist[11]))

print(jose_user.like_song(bieber.albums['changes'].songs_playlist[11]))

print(jose_user.like_song(bieber.albums['changes'].songs_playlist[3]))

print(jose_user.like_song(minaj.albums['queen'].songs_playlist[3]))

print(jose_user.like_song(minaj.albums['queen'].songs_playlist[15]))

print()

print(jose_user.create_playlist('music_new'))

print(jose_user.playlists['music_new'].add_song(bieber.albums['changes'].songs_playlist[6]))

print(jose_user.playlists['music_new'].add_song(bieber.albums['changes'].songs_playlist[2]))

print(jose_user.playlists['music_new'].add_song(bieber.albums['changes'].songs_playlist[5]))

print(jose_user.playlists['music_new'].add_song(bieber.albums['changes'].songs_playlist[0]))

print(jose_user.playlists['music_new'].add_song(bieber.albums['changes'].songs_playlist[8]))

print(jose_user.playlists['music_new'].add_song(bieber.albums['changes'].songs_playlist[10]))

print(jose_user.playlists['music_new'].add_song(bieber.albums['changes'].songs_playlist[1]))

print(jose_user.playlists['music_new'].add_song(lipa.albums['dualipa_deluxe'].songs_playlist[2]))

print(jose_user.playlists['music_new'].add_song(lipa.albums['dualipa_deluxe'].songs_playlist[9]))

# print(jose_user.playlists['music_new'].add_song(lipa.albums['dualipa_deluxe'].songs_playlist[5]))

# print(jose_user.playlists['music_new'].add_song(lipa.albums['dualipa_deluxe'].songs_playlist[3]))

# print(jose_user.playlists['music_new'].add_song(minaj.albums['queen'].songs_playlist[2]))

# print(jose_user.playlists['music_new'].add_song(minaj.albums['queen'].songs_playlist[8]))

# print(jose_user.playlists['music_new'].add_song(minaj.albums['queen'].songs_playlist[1]))

# print(jose_user.playlists['music_new'].add_song(minaj.albums['queen'].songs_playlist[12]))

print()

jose_user.playlists['music_new'].show_songs()

print()

jose_user.playlists['liked_songs'].show_songs()

print()

# jose_user.play_playlist()

print('----------------------------------')
print('----------------------------------')